from datetime import datetime, timezone
from app.models.enums import SourceTier
from app.models.schemas import SourceMetadata, EvidenceChunk
from app.ranking.scorer import score


def test_primary_source_gets_authority():
    s = SourceMetadata(url="https://osfi-bsif.gc.ca/x", domain="osfi-bsif.gc.ca", title="LAR",
        retrieved_at=datetime.now(timezone.utc), tier=SourceTier.T1_PRIMARY, jurisdiction="Canada",
        primary_source=True, content_hash="abc")
    c = EvidenceChunk(source=s, chunk_id="1", text="liquidity", lexical_score=1)
    out=score(c,"Canada")
    assert out.authority_score == 1
    assert out.final_score > 0.7
