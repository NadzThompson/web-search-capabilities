# Deployment Runbook

1. Create dedicated runtime identity for the search API and crawler.
2. Provision private application runtime, ADLS container, Elastic/PGVector connectivity, observability and approved outbound proxy/firewall rules.
3. Register enterprise DLP/classification integrations.
4. Configure Key Vault / managed identity; do not place secrets in `.env` for production.
5. Create `raw`, `parsed`, `quarantine`, `evidence`, `versions` storage zones.
6. Apply Elastic mapping and PGVector schema.
7. Deploy search API with live crawling disabled.
8. Deploy crawler as a separate workload with approved outbound egress.
9. Connect Databricks enrichment jobs and Unity Catalog governance.
10. Run unit, integration, DLP, SSRF, prompt-injection, canary-leakage and load tests.
11. Validate logs contain hashes/metadata rather than raw proprietary queries.
12. Enable production only after Security, Privacy, Architecture, Model Validation and Operations sign-off.

## Rollback

Disable crawler egress, set live fetch false, disable any external provider adapters and continue serving from the last approved internal index.
