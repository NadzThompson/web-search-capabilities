# Updated Implementation Plan

1. Merge the new `app/skills/` package into the NOVA codebase.
2. Replace the current `web_search_agent.py` with/merge into `app/agents/web_search_agent.py` while preserving your existing public interface.
3. Replace the existing Web Search Agent system prompt with `prompts/web_search_agent_system_prompt.md` after regression review.
4. Integrate `app/graph/web_search_graph.py` as a specialist subgraph under the existing platform LangGraph supervisor.
5. Connect enterprise DLP/classification and remove reliance on reference-only detection for production.
6. Enforce outbound network policy so agents cannot bypass Search Gateway/crawler.
7. Configure ADLS zones and service identities.
8. Deploy Databricks parse/enrich/embed jobs.
9. Wire Elastic + PGVector production adapters; connect graph layer.
10. Populate and govern the source registry.
11. Build Treasury benchmark and adversarial security suites.
12. Add model/prompt/skill/policy versions to audit traces.
13. Run architecture, security, privacy, legal/licensing, model-validation, and operational-readiness reviews.
14. Pilot with STRICT/TRUSTED/OPEN modes and controlled live retrieval.
