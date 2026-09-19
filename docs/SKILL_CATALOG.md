# NOVA Web Search Skill Catalog

## Purpose
This document defines the reusable capability layer beneath the Web Search Agent. LangGraph is the platform-level orchestrator. Agents own domain responsibility. Skills are bounded capabilities. Mandatory security services are not optional and cannot be bypassed by an LLM or routing decision.

## The 16 skills

| # | Skill | Module | Purpose | Mandatory |
|---|---|---|---|---|
| 1 | Search Intent | `app/skills/search_intent.py` | Classify regulatory, macro, company, markets, research, innovation, open-web intent | No |
| 2 | Query Security | `app/skills/query_security.py` | Invoke classification + policy gateway | Yes |
| 3 | Query Abstraction | `app/skills/query_abstraction.py` | Convert non-public queries into public-safe queries and reclassify | Yes when transformed |
| 4 | Search Planning | `app/skills/search_planning.py` | Produce bounded subqueries | No |
| 5 | Source Policy | `app/skills/source_policy.py` | Select STRICT/TRUSTED/OPEN | Yes |
| 6 | Web Retrieval | `app/skills/web_retrieval.py` | Search NOVA index, optional controlled provider fallback | No |
| 7 | Crawler/Freshness | `app/skills/crawler_freshness.py` | Determine staleness and refresh need | No |
| 8 | Prompt Injection Screening | `app/skills/prompt_injection_screening.py` | Sanitize and quarantine external content | Yes |
| 9 | Source Trust | `app/skills/source_trust.py` | Tier and classify sources | Yes |
| 10 | Hybrid Retrieval | `app/skills/hybrid_retrieval.py` | Fuse lexical + semantic retrieval | No |
| 11 | Evidence Reranking | `app/skills/evidence_reranking.py` | Rank by relevance, authority, primary source, freshness, jurisdiction, corroboration | No |
| 12 | Corroboration | `app/skills/corroboration.py` | Measure source diversity / corroboration | No |
| 13 | Citation Verification | `app/skills/citation_verification.py` | Verify that claims are supported by cited evidence | Yes for answer generation |
| 14 | Evidence Sufficiency | `app/skills/evidence_sufficiency.py` | Decide answer vs retrieve-more | Yes |
| 15 | Audit/Lineage | `app/skills/audit_lineage.py` | Record safe decision and evidence lineage | Yes |
| 16 | Output DLP | `app/skills/output_dlp.py` | Prevent sensitive data from leaving the final response boundary | Yes |

## Design contract
A skill must be:
- small and testable;
- side-effect free unless the purpose requires a controlled side effect;
- deterministic where security or policy is involved;
- explicit about inputs and outputs;
- independently unit-testable;
- callable from LangGraph nodes or agents without embedding orchestration logic inside the skill.

## Mandatory controls
The following are mandatory execution gates and must not be represented as optional LLM choices:
- query classification and DLP;
- egress policy;
- prompt-injection screening for retrieved content;
- SSRF/private-network enforcement;
- source policy where required;
- citation verification before material factual claims are finalized;
- evidence sufficiency gate;
- output DLP;
- audit/lineage.
