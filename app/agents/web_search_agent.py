from __future__ import annotations
import uuid
from app.models.enums import Decision
from app.skills import search_intent, query_security, query_abstraction, search_planning, source_policy
from app.skills import web_retrieval, evidence_reranking, corroboration, evidence_sufficiency, audit_lineage

class WebSearchAgent:
    """Domain agent invoked by the top-level NOVA LangGraph orchestrator.

    Hard security decisions are delegated to deterministic gateway/services and are not
    left to the LLM or agent discretion.
    """
    def __init__(self, index, external_provider=None):
        self.index = index
        self.external_provider = external_provider

    async def execute(self, state: dict) -> dict:
        request_id = state.get('request_id') or str(uuid.uuid4())
        query = state['original_query']
        jurisdiction = state.get('jurisdiction')

        security = query_security.run(query)
        data = security.data
        audit_lineage.run('web_search_security_decision', request_id, query=query,
                          decision=data['decision'], classification=data['classification'],
                          content_types=data['content_types'])
        if data['decision'] == Decision.BLOCK.value:
            return {**state, 'request_id': request_id, 'policy_decision': data['decision'],
                    'classification': data['classification'], 'content_types': data['content_types'],
                    'blocked_reason': data.get('blocked_reason') or 'SEARCH_BLOCKED_BY_POLICY',
                    'evidence': [], 'warnings': ['SEARCH_BLOCKED_BY_POLICY']}

        safe_query = data.get('safe_query') or query
        if data['decision'] == Decision.TRANSFORM.value:
            abstraction = query_abstraction.run(query)
            if not abstraction.ok or not abstraction.data.get('safe_query'):
                return {**state, 'request_id': request_id, 'policy_decision': Decision.BLOCK.value,
                        'blocked_reason': 'SAFE_QUERY_TRANSFORMATION_FAILED', 'evidence': [],
                        'warnings': ['SAFE_QUERY_TRANSFORMATION_FAILED']}
            safe_query = abstraction.data['safe_query']

        intent = search_intent.run(safe_query).data['intent']
        mode = source_policy.run(intent, state.get('search_mode')).data['mode']
        plans = search_planning.run(safe_query, intent, jurisdiction).data['queries']

        all_chunks = []
        for q in plans:
            retrieved = await web_retrieval.run(q, self.index, state.get('top_k', 10), self.external_provider)
            all_chunks.extend(retrieved.data['chunks'])
        # dedupe by chunk id
        dedup = {c.chunk_id: c for c in all_chunks}
        corr = corroboration.run(list(dedup.values()))
        ranked = evidence_reranking.run(corr.data['chunks'], jurisdiction, state.get('top_k', 10)).data['chunks']
        suff = evidence_sufficiency.run(ranked)

        return {**state, 'request_id': request_id, 'safe_query': safe_query,
                'classification': data['classification'], 'content_types': data['content_types'],
                'policy_decision': data['decision'], 'intent': intent, 'search_mode': mode,
                'planned_queries': plans, 'evidence': ranked,
                'evidence_sufficient': suff.data['sufficient'],
                'warnings': list(dict.fromkeys(state.get('warnings', []) + corr.warnings + suff.warnings))}
