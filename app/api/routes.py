import yaml
from fastapi import APIRouter, HTTPException
from app.config import settings
from app.models.schemas import SearchRequest, SearchResponse, CrawlRequest, CrawlResult
from app.orchestrator import SearchOrchestrator
from app.indexing.memory import MemoryIndex
from app.storage.local import LocalEvidenceStore
from app.crawler.service import CrawlService

router = APIRouter()
_index = MemoryIndex()
_orchestrator = SearchOrchestrator(index=_index)
try:
    _source_registry = yaml.safe_load(settings.nova_source_registry.read_text()) or {}
except Exception:
    _source_registry = {}
_crawler = CrawlService(LocalEvidenceStore(), _index, _source_registry)

@router.get("/health")
async def health():
    return {"status":"ok","service":"nova-web-search","version":"4.0.0"}

@router.post("/v1/search", response_model=SearchResponse)
async def search(req: SearchRequest):
    return await _orchestrator.search(req)

@router.post("/v1/crawl", response_model=CrawlResult)
async def crawl(req: CrawlRequest):
    if not settings.nova_allow_live_fetch:
        raise HTTPException(status_code=403, detail="Live fetch disabled by policy")
    try:
        return await _crawler.crawl(str(req.url), req.force)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
