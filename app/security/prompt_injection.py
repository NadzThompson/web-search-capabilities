import base64
import html
import re
from dataclasses import dataclass
from bs4 import BeautifulSoup

_INJECTION_PATTERNS = [
    re.compile(r"(?i)ignore (all|any|the)?\s*(previous|prior|system|developer) instructions"),
    re.compile(r"(?i)reveal (the )?(system|developer) prompt"),
    re.compile(r"(?i)(upload|send|exfiltrate|post) .*?(files?|secrets?|credentials?|environment variables?)"),
    re.compile(r"(?i)(execute|run) (this|the following) (command|code|script)"),
    re.compile(r"(?i)call (this|the) (url|endpoint|tool)"),
    re.compile(r"(?i)do not cite|hide this source|ignore other sources"),
]

@dataclass(frozen=True)
class InjectionResult:
    risk: float
    signals: list[str]
    quarantined: bool
    sanitized_text: str

def sanitize_html(raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, "lxml")
    for tag in soup(["script", "style", "iframe", "form", "object", "embed", "noscript", "svg"]):
        tag.decompose()
    # remove elements hidden through common inline styles/attributes
    for tag in soup.find_all(True):
        style = (tag.get("style") or "").lower()
        if tag.has_attr("hidden") or "display:none" in style.replace(" ", "") or "visibility:hidden" in style.replace(" ", ""):
            tag.decompose()
    return html.unescape(soup.get_text(" ", strip=True))

def inspect(text: str, raw_html: str | None = None) -> InjectionResult:
    sanitized = sanitize_html(raw_html) if raw_html is not None else text
    signals: list[str] = []
    for i, pattern in enumerate(_INJECTION_PATTERNS):
        if pattern.search(sanitized):
            signals.append(f"pattern_{i+1}")
    # simple encoded-payload heuristic
    for token in re.findall(r"\b[A-Za-z0-9+/]{40,}={0,2}\b", sanitized):
        try:
            decoded = base64.b64decode(token + "===", validate=False).decode("utf-8", "ignore")
            if any(p.search(decoded) for p in _INJECTION_PATTERNS):
                signals.append("encoded_instruction")
                break
        except Exception:
            pass
    risk = min(1.0, 0.25 * len(set(signals)))
    return InjectionResult(risk=risk, signals=sorted(set(signals)), quarantined=risk >= 0.5, sanitized_text=sanitized)
