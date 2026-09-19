from app.audit.logger import record, query_hash
from app.skills.types import SkillResult

def run(event_type: str, request_id: str, query: str | None = None, **metadata) -> SkillResult:
    if query is not None:
        metadata['query_hash'] = query_hash(query)
    record(event_type, request_id=request_id, **metadata)
    return SkillResult(True, {'recorded': True, 'event_type': event_type})
