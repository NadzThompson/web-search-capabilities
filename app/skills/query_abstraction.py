from app.security.abstraction import abstract_query
from app.security.classifier import classify
from app.skills.types import SkillResult

def run(query: str) -> SkillResult:
    before = classify(query)
    safe = abstract_query(query)
    after = classify(safe)
    # fail closed if transformation still produces sensitive-or-higher text
    blocked = after.classification.value in {'restricted','sensitive'}
    return SkillResult(not blocked, {
        'safe_query': None if blocked else safe,
        'before_classification': before.classification.value,
        'after_classification': after.classification.value,
        'after_content_types': [x.value for x in after.content_types],
    }, errors=['abstraction_not_safe'] if blocked else [])
