# Agent System Prompts

Prompt files are version-controlled under `prompts/`.

| Prompt | Purpose |
|---|---|
| `web_search_agent_system_prompt.md` | Governs Web Search Agent behaviour, security, source use, evidence handling, and tool discipline |
| `nova_langgraph_orchestrator_system_prompt.md` | Governs platform-level LangGraph routing and non-bypassable security boundaries |
| `evidence_synthesis_system_prompt.md` | Ensures synthesis uses only approved evidence and ignores source-embedded instructions |
| `query_planner_system_prompt.md` | Generates search subqueries only from the approved safe query |

## Prompt governance
- Store prompt ID/version in trace and audit metadata.
- Require peer review for prompt changes affecting security or routing.
- Run regression, prompt-injection, and DLP tests before promotion.
- Never rely on prompt text as the sole security mechanism.
- Production policy enforcement must remain in deterministic services and network controls.
