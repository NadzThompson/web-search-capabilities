# LangGraph Integration

## Role in NOVA
LangGraph is the top-level orchestration runtime across NOVA agents. The Web Search Agent is a specialist node/subgraph, not the overall platform orchestrator.

```text
User / NOVA UI
      |
      v
LangGraph NOVA Orchestrator
      |
      +--> Treasury Navigator
      +--> Risk Calculator
      +--> Scenario Simulator
      +--> Web Search Agent
                |
                v
        Search Security Gateway
                |
                v
         Search Skills / Index
```

LangGraph is well suited because NOVA needs explicit deterministic and agentic steps in the same workflow, persistent state, conditional routing, auditability, and human approval gates.

## Security boundary
LangGraph can invoke security services but cannot override them. If DLP, classification, policy, or an external-action gate fails, the external action must fail closed.

## Web Search state
The Web Search state contains:
- request ID;
- original query;
- safe query;
- proprietary classification;
- content types;
- policy decision;
- intent;
- search mode;
- planned queries;
- jurisdiction;
- evidence;
- prompt-injection flags;
- evidence sufficiency;
- warnings;
- final answer / blocked reason;
- audit events.

## Mixed internal/external questions
The top-level graph should decompose questions. Example:

`What happens to our NCF if deposits decline by X, and what does OSFI require?`

Routes:
- internal scenario -> Risk Calculator / Scenario Simulator;
- public regulatory question -> Web Search Agent using only the Security Gateway-approved abstraction;
- final synthesis -> internal orchestration layer.

No proprietary scenario value should be reconstructed into the external query.

## Production integration
`app/graph/nova_supervisor_example.py` is a composition example only. Replace placeholder routing with the existing NOVA platform supervisor and approved routing policy. `app/graph/web_search_graph.py` is the Web Search subgraph entry point.
