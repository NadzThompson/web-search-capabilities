from app.models.enums import SearchMode, SourceTier
from app.models.schemas import EvidenceChunk

_ALLOWED = {
    SearchMode.STRICT: {SourceTier.T1_PRIMARY, SourceTier.T2_INSTITUTIONAL},
    SearchMode.TRUSTED: {SourceTier.T1_PRIMARY, SourceTier.T2_INSTITUTIONAL, SourceTier.T3_ESTABLISHED, SourceTier.T4_COMMENTARY},
    SearchMode.OPEN: set(SourceTier),
}

def filter_by_mode(chunks: list[EvidenceChunk], mode: SearchMode, allowed_domains: list[str] | None = None) -> list[EvidenceChunk]:
    tiers = _ALLOWED[mode]
    domains = {d.lower() for d in (allowed_domains or [])}
    out=[]
    for c in chunks:
        if c.source.tier not in tiers:
            continue
        if domains and c.source.domain.lower() not in domains:
            continue
        out.append(c)
    return out
