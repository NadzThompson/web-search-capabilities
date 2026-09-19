# NOVA Web Search Agent v4

A NOVA-owned web research and evidence-retrieval stack for Corporate Treasury. The design keeps user queries inside NOVA by default, maintains a curated internal web index, supports controlled crawling and live retrieval, and treats all external content as untrusted evidence.

## Security principles

1. Proprietary hierarchy: **Restricted → Sensitive → Confidential → Internal → Public**.
2. Content type is separate from classification (client, counterparty, position, balance, exposure, forecast, PII, credential, etc.).
3. Raw non-public queries do not leave NOVA.
4. Restricted data, secrets, authentication data, customer PII and payment data fail closed.
5. External content is never instruction-authoritative.
6. Prompt-injection detection is only one layer; least privilege, egress controls, SSRF controls, content sanitization, quarantine and output DLP provide defense in depth.
7. The internal NOVA index is primary. External search providers are optional adapters only.

## Components

- FastAPI search/crawl API
- Search Security Gateway
- DLP and classification reference implementation
- Query abstraction
- SSRF/public-network validation
- Web crawler with redirect and size controls
- Prompt injection firewall and quarantine
- Source registry and trust tiers
- Evidence chunking/version hashes
- In-memory and Elastic adapters
- PGVector schema
- ADLS adapter
- Databricks processing job skeletons
- Treasury-aware ranking
- Audit events with query hashing
- Docker/Kubernetes/Bicep scaffolding
- Unit/security tests

## Quick start

```bash
cp .env.example .env
python -m pip install -e '.[dev]'
pytest -q
uvicorn app.main:app --reload --port 8080
```

Live web fetching is disabled by default. To test crawling in a controlled development environment, set `NOVA_ALLOW_LIVE_FETCH=true`.

## Production warning

This repository is a production-oriented reference implementation. Before GSIB production deployment, integrate bank-approved enterprise DLP/classification, malware scanning, document sandboxing, SIEM, identity/RBAC, outbound proxy/firewall, certificate management, secrets management, embedding/model endpoints, and approved data-retention controls.

## v5 additions: LangGraph + Skill Layer
This revision adds sixteen reusable Web Search skills, a LangGraph-compatible Web Search Agent/subgraph, top-level NOVA supervisor composition example, and version-controlled system prompts. See `docs/SKILL_CATALOG.md`, `docs/LANGGRAPH_INTEGRATION.md`, and `prompts/`.
