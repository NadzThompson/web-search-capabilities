from app.models.schemas import EvidenceChunk

def validate_evidence(chunks: list[EvidenceChunk]) -> tuple[list[EvidenceChunk], list[str]]:
    warnings=[]
    safe=[c for c in chunks if c.source.injection_risk < 0.5 and c.text.strip()]
    domains={c.source.domain for c in safe}
    if len(domains) < 2 and len(safe) > 1:
        warnings.append("limited_source_diversity")
    if not safe:
        warnings.append("insufficient_safe_evidence")
    return safe, warnings
