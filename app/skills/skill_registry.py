from dataclasses import dataclass

@dataclass(frozen=True)
class SkillSpec:
    name: str
    module: str
    mandatory: bool
    deterministic: bool
    purpose: str

SKILLS = [
    SkillSpec('search_intent','app.skills.search_intent',False,True,'Classify search intent.'),
    SkillSpec('query_security','app.skills.query_security',True,True,'Enforce proprietary-data search policy.'),
    SkillSpec('query_abstraction','app.skills.query_abstraction',True,True,'Transform non-public queries to public-safe queries.'),
    SkillSpec('search_planning','app.skills.search_planning',False,True,'Create bounded search subqueries.'),
    SkillSpec('source_policy','app.skills.source_policy',True,True,'Select strict/trusted/open source mode.'),
    SkillSpec('web_retrieval','app.skills.web_retrieval',False,True,'Retrieve from NOVA indexes/providers.'),
    SkillSpec('crawler_freshness','app.skills.crawler_freshness',False,True,'Decide whether evidence is stale.'),
    SkillSpec('prompt_injection_screening','app.skills.prompt_injection_screening',True,True,'Screen external content for prompt injection.'),
    SkillSpec('source_trust','app.skills.source_trust',True,True,'Assign source trust tier.'),
    SkillSpec('hybrid_retrieval','app.skills.hybrid_retrieval',False,True,'Fuse lexical and semantic retrieval.'),
    SkillSpec('evidence_reranking','app.skills.evidence_reranking',False,True,'Rerank by relevance, authority, freshness, jurisdiction.'),
    SkillSpec('corroboration','app.skills.corroboration',False,True,'Measure cross-source corroboration.'),
    SkillSpec('citation_verification','app.skills.citation_verification',True,True,'Verify claim-to-evidence support.'),
    SkillSpec('evidence_sufficiency','app.skills.evidence_sufficiency',True,True,'Decide whether evidence is sufficient.'),
    SkillSpec('audit_lineage','app.skills.audit_lineage',True,True,'Record safe audit lineage.'),
    SkillSpec('output_dlp','app.skills.output_dlp',True,True,'Prevent sensitive output leakage.'),
]
