from collections import defaultdict
from app.skills.types import SkillResult

def run(chunks: list) -> SkillResult:
    domains = {c.source.domain for c in chunks}
    score = min(1.0, len(domains) / 3.0)
    for c in chunks:
        c.corroboration_score = score
    warnings = [] if len(domains) >= 2 else ['single_source_only']
    return SkillResult(True, {'chunks': chunks, 'unique_domains': len(domains), 'corroboration_score': score}, warnings=warnings)
