from app.security.gateway import evaluate
from app.skills.types import SkillResult

def run(query: str) -> SkillResult:
    g = evaluate(query)
    return SkillResult(True, {
        'decision': g.decision.value,
        'classification': g.original_classification.classification.value,
        'content_types': [x.value for x in g.original_classification.content_types],
        'safe_query': g.safe_query,
        'blocked_reason': g.blocked_reason,
        'reasons': g.original_classification.reasons,
    })
