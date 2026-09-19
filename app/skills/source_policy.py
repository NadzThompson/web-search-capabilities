from app.models.enums import SearchMode
from app.skills.types import SkillResult

DEFAULT_MODE = {
    'regulatory': SearchMode.STRICT,
    'macroeconomic': SearchMode.STRICT,
    'company': SearchMode.TRUSTED,
    'markets': SearchMode.TRUSTED,
    'research': SearchMode.TRUSTED,
    'innovation': SearchMode.OPEN,
    'open_web': SearchMode.OPEN,
}

def run(intent: str, requested_mode: str | None = None) -> SkillResult:
    mode = SearchMode(requested_mode) if requested_mode else DEFAULT_MODE.get(intent, SearchMode.TRUSTED)
    return SkillResult(True, {'mode': mode.value})
