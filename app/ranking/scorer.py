from datetime import datetime, timezone
from app.models.schemas import EvidenceChunk

TIER_SCORE = {
    "t1_primary": 1.0,
    "t2_institutional": 0.9,
    "t3_established": 0.75,
    "t4_commentary": 0.6,
    "t5_general": 0.4,
    "t6_unverified": 0.2,
}

def score(chunk: EvidenceChunk, jurisdiction: str | None = None) -> EvidenceChunk:
    c = chunk.model_copy(deep=True)
    c.authority_score = TIER_SCORE.get(c.source.tier.value, 0.2)
    if c.source.published_at:
        age_days = max(0, (datetime.now(timezone.utc) - c.source.published_at.astimezone(timezone.utc)).days)
        c.freshness_score = max(0.0, 1.0 - min(age_days, 3650) / 3650)
    else:
        c.freshness_score = 0.5
    c.jurisdiction_score = 1.0 if jurisdiction and c.source.jurisdiction and c.source.jurisdiction.lower() == jurisdiction.lower() else (0.5 if jurisdiction else 1.0)
    semantic = c.semantic_score
    lexical = c.lexical_score
    relevance = max(lexical, semantic)
    primary = 1.0 if c.source.primary_source else 0.0
    c.final_score = (
        0.30 * relevance + 0.25 * c.authority_score + 0.15 * primary +
        0.10 * c.freshness_score + 0.10 * c.jurisdiction_score + 0.10 * c.corroboration_score
    )
    if c.source.injection_risk >= 0.5:
        c.final_score = 0.0
    return c
