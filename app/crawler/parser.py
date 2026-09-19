from bs4 import BeautifulSoup
from app.security.prompt_injection import inspect

ALLOWED_CONTENT_TYPES = {"text/html", "text/plain", "application/pdf", "application/xml", "text/xml", "application/rss+xml"}

def parse_html(raw: bytes) -> tuple[str, str, float, list[str], bool]:
    html = raw.decode("utf-8", "replace")
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    inj = inspect("", raw_html=html)
    return title, inj.sanitized_text, inj.risk, inj.signals, inj.quarantined
