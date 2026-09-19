import httpx
from dataclasses import dataclass
from urllib.parse import urljoin
from app.config import settings
from app.security.network import validate_public_url

@dataclass
class FetchResult:
    final_url: str
    status_code: int
    content_type: str
    body: bytes
    headers: dict[str, str]

async def fetch(url: str) -> FetchResult:
    validate_public_url(url)
    timeout = httpx.Timeout(settings.nova_fetch_timeout_seconds)
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=False, headers={"User-Agent":"NOVA-Web-Crawler/1.0"}) as client:
        current = url
        for _ in range(5):
            validate_public_url(current)
            async with client.stream("GET", current) as resp:
                if resp.status_code in {301,302,303,307,308}:
                    location = resp.headers.get("location")
                    if not location:
                        break
                    current = urljoin(current, location)
                    continue
                data = bytearray()
                async for chunk in resp.aiter_bytes():
                    data.extend(chunk)
                    if len(data) > settings.nova_max_fetch_bytes:
                        raise ValueError("response_too_large")
                ctype = resp.headers.get("content-type", "application/octet-stream").split(";")[0].strip().lower()
                return FetchResult(str(resp.url), resp.status_code, ctype, bytes(data), dict(resp.headers))
        raise ValueError("too_many_redirects")
