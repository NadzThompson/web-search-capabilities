import hashlib
from datetime import datetime, timezone
from urllib.parse import urlparse
from app.crawler.fetcher import fetch
from app.crawler.robots import allowed
from app.crawler.parser import parse_html, ALLOWED_CONTENT_TYPES
from app.evidence.chunker import chunk_text
from app.models.enums import SourceTier
from app.models.schemas import CrawlResult, EvidenceChunk, SourceMetadata
from app.security.network import validate_public_url
from app.audit.logger import record

class CrawlService:
    def __init__(self, store, index, source_registry):
        self.store = store
        self.index = index
        self.source_registry = source_registry

    async def crawl(self, url: str, force: bool = False) -> CrawlResult:
        validate_public_url(url)
        if not force and not await allowed(url):
            return CrawlResult(url=url, status="blocked", stored=False, quarantined=False, reason="robots_disallow")
        fr = await fetch(url)
        if fr.content_type not in ALLOWED_CONTENT_TYPES:
            return CrawlResult(url=url, status="blocked", stored=False, quarantined=False, reason="unsupported_content_type")
        content_hash = hashlib.sha256(fr.body).hexdigest()
        key = f"{content_hash[:2]}/{content_hash}"
        await self.store.put_raw(key, fr.body, fr.content_type)
        domain = urlparse(fr.final_url).hostname or ""
        source_cfg = self.source_registry.get(domain, {})
        if fr.content_type == "text/html":
            title, text, risk, signals, quarantined = parse_html(fr.body)
        elif fr.content_type == "text/plain":
            title, text, risk, signals, quarantined = "", fr.body.decode("utf-8","replace"), 0.0, [], False
        else:
            # PDF/XML production parsing is delegated to sandboxed document processors / Databricks jobs.
            return CrawlResult(url=fr.final_url, status="stored_raw", stored=True, quarantined=False,
                               reason="requires_async_document_parser", metadata={"content_hash":content_hash, "content_type":fr.content_type})
        if quarantined:
            record("content_quarantined", url=fr.final_url, content_hash=content_hash, signals=signals, injection_risk=risk)
            return CrawlResult(url=fr.final_url, status="quarantined", stored=True, quarantined=True,
                               reason="prompt_injection_risk", metadata={"content_hash":content_hash, "signals":signals})
        await self.store.put_text(key, text)
        meta = SourceMetadata(url=fr.final_url, domain=domain, title=title,
                              publisher=source_cfg.get("publisher"), published_at=None,
                              retrieved_at=datetime.now(timezone.utc),
                              tier=SourceTier(source_cfg.get("tier", "t6_unverified")),
                              jurisdiction=source_cfg.get("jurisdiction"),
                              primary_source=bool(source_cfg.get("primary_source", False)),
                              content_hash=content_hash, injection_risk=risk)
        chunks=[EvidenceChunk(source=meta, chunk_id=f"{content_hash}:{i}", text=t) for i,t in enumerate(chunk_text(text))]
        await self.index.upsert(chunks)
        record("content_indexed", url=fr.final_url, content_hash=content_hash, chunks=len(chunks))
        return CrawlResult(url=fr.final_url, status="indexed", stored=True, quarantined=False, metadata={"content_hash":content_hash,"chunks":len(chunks)})
