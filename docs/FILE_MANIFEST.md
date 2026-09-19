# File Manifest

## Runtime code
- `app/main.py` FastAPI entrypoint
- `app/orchestrator.py` search flow
- `app/security/*` classification, DLP, abstraction, prompt-injection, SSRF, output DLP
- `app/policy/*` egress and source/search-mode policy
- `app/crawler/*` fetch, robots, parse, crawl/index service
- `app/storage/*` local and ADLS evidence stores
- `app/indexing/*` in-memory, Elastic and PGVector adapters
- `app/ranking/*` Treasury evidence scoring
- `app/evidence/*` chunking, validation and citation verification
- `app/audit/*` safe audit telemetry
- `app/providers/*` optional external-provider interface

## Configuration
- `config/policy.yaml`
- `config/source_registry.yaml`
- `config/source_registry.schema.json`
- `config/crawl_schedule.yaml`
- `.env.example`

## Data/search schemas
- `sql/pgvector_schema.sql`
- `sql/elastic_mapping.json`

## Databricks
- `databricks/01_parse_enrich.py`
- `databricks/02_embed_publish.py`

## Infrastructure
- `Dockerfile`, `docker-compose.yml`
- `infrastructure/bicep/main.bicep`
- `infrastructure/k8s/deployment.yaml`
- `infrastructure/k8s/network-policy.yaml`
- `.github/workflows/ci.yml`

## Documentation
Architecture, security, prompt injection, source governance, ADLS/Databricks, API, deployment, validation, production readiness, system prompt and next steps are under `docs/`.
