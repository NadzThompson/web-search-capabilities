from urllib import robotparser
from urllib.parse import urlparse
import httpx

async def allowed(url: str, user_agent: str = "NOVA-Web-Crawler") -> bool:
    p = urlparse(url)
    robots_url = f"{p.scheme}://{p.netloc}/robots.txt"
    rp = robotparser.RobotFileParser()
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(robots_url, headers={"User-Agent": user_agent})
        if r.status_code >= 400:
            return True
        rp.set_url(robots_url)
        rp.parse(r.text.splitlines())
        return rp.can_fetch(user_agent, url)
    except Exception:
        # Enterprise policy may choose stricter behavior per source. Default here is conservative allow only for unavailable robots endpoint.
        return True
