import time, uuid
from app.audit.logger import record, query_hash
from app.indexing.memory import MemoryIndex
from app.models.enums import Decision
from app.models.schemas import SearchRequest, SearchResponse
from app.ranking.scorer import score
from app.security.gateway import evaluate
from app.evidence.validator import validate_evidence
from app.policy.source_policy import filter_by_mode

class SearchOrchestrator:
    def __init__(self, index=None, external_provider=None):
        self.index = index or MemoryIndex()
        self.external_provider = external_provider

    async def search(self, req: SearchRequest) -> SearchResponse:
        start = time.perf_counter()
        request_id = str(uuid.uuid4())
        gate = evaluate(req.query)
        record("search_gateway_decision", request_id=request_id, query_hash=query_hash(req.query), decision=gate.decision.value,
               classification=gate.original_classification.classification.value,
               content_types=[x.value for x in gate.original_classification.content_types])
        if gate.decision == Decision.BLOCK:
            return SearchResponse(request_id=request_id, decision=gate.decision, safe_query=None,
                                  evidence=[], warnings=[gate.blocked_reason or "blocked"],
                                  latency_ms=int((time.perf_counter()-start)*1000))
        safe_query = gate.safe_query or req.query
        results = await self.index.search(safe_query, req.top_k)
        if not results and self.external_provider is not None:
            results = await self.external_provider.search(safe_query, req.top_k)
        results = filter_by_mode(results, req.mode, req.allowed_domains)
        ranked = [score(c, req.jurisdiction) for c in results]
        ranked.sort(key=lambda c: c.final_score, reverse=True)
        safe, warnings = validate_evidence(ranked[:req.top_k])
        return SearchResponse(request_id=request_id, decision=gate.decision, safe_query=safe_query,
                              evidence=safe, warnings=warnings,
                              latency_ms=int((time.perf_counter()-start)*1000))
