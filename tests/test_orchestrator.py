from datetime import datetime, timezone
import pytest
from app.indexing.memory import MemoryIndex
from app.models.enums import SourceTier, Decision
from app.models.schemas import SourceMetadata, EvidenceChunk, SearchRequest
from app.orchestrator import SearchOrchestrator

@pytest.mark.asyncio
async def test_search_internal_index():
    idx=MemoryIndex()
    s=SourceMetadata(url="https://bis.org/a",domain="bis.org",title="Basel liquidity",
        retrieved_at=datetime.now(timezone.utc),tier=SourceTier.T1_PRIMARY,primary_source=True,content_hash="h")
    await idx.upsert([EvidenceChunk(source=s,chunk_id="h:0",text="Basel liquidity coverage ratio standard")])
    r=await SearchOrchestrator(idx).search(SearchRequest(query="Basel liquidity coverage ratio"))
    assert r.decision == Decision.ALLOW
    assert r.evidence
