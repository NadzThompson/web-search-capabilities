from app.security.prompt_injection import inspect
from app.skills.types import SkillResult

def run(text: str, raw_html: str | None = None) -> SkillResult:
    r = inspect(text, raw_html)
    return SkillResult(not r.quarantined, {
        'risk': r.risk,
        'signals': r.signals,
        'quarantined': r.quarantined,
        'sanitized_text': r.sanitized_text,
    }, warnings=['prompt_injection_risk'] if r.signals else [])
