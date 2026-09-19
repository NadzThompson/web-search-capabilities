from app.skills.types import SkillResult

def run(chunks: list, min_chunks: int = 2, min_domains: int = 2, min_score: float = 0.35) -> SkillResult:
    usable = [c for c in chunks if c.final_score >= min_score and c.source.injection_risk < 0.5]
    domains = {c.source.domain for c in usable}
    sufficient = len(usable) >= min_chunks and len(domains) >= min_domains
    return SkillResult(sufficient, {
        'sufficient': sufficient,
        'usable_chunks': len(usable),
        'unique_domains': len(domains),
        'recommended_action': 'answer' if sufficient else 'retrieve_more',
    }, warnings=[] if sufficient else ['insufficient_evidence'])
