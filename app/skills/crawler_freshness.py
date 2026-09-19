from __future__ import annotations
from datetime import datetime, timezone
from app.skills.types import SkillResult

DEFAULT_HOURS = {
    'regulatory': 6,
    'macroeconomic': 6,
    'company': 6,
    'markets': 1,
    'research': 168,
    'innovation': 24,
    'open_web': 24,
}

def run(last_retrieved_at: datetime | None, intent: str, override_hours: int | None = None) -> SkillResult:
    ttl = override_hours or DEFAULT_HOURS.get(intent, 24)
    if last_retrieved_at is None:
        return SkillResult(True, {'refresh_required': True, 'ttl_hours': ttl})
    age = (datetime.now(timezone.utc) - last_retrieved_at.astimezone(timezone.utc)).total_seconds() / 3600
    return SkillResult(True, {'refresh_required': age > ttl, 'age_hours': age, 'ttl_hours': ttl})
