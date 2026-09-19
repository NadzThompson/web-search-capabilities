# Production Readiness

## Included in this repository

- reference classification/DLP
- query abstraction and fail-closed policy
- SSRF/public-network validation
- crawler controls
- prompt-injection sanitization/quarantine
- trust tiers/ranking
- ADLS adapter
- Elastic adapter and PGVector schema
- Databricks skeleton jobs
- audit hashing
- Docker/Kubernetes/Bicep scaffolding
- tests and runbooks

## Required enterprise integrations before production

- bank-approved DLP and information-classification services
- approved PII/secrets scanners
- malware and content-disarm/sandbox services
- hardened PDF/Office parsing
- Azure Firewall/proxy/FQDN governance and private DNS design
- enterprise RBAC/Entra groups and managed identities
- Key Vault / certificate management
- SIEM and SOC alerting
- approved embedding/model endpoints
- retention/legal-hold policies
- formal source licensing/terms review
- SLOs, autoscaling, capacity and DR
- penetration testing and independent red-team review
- model validation / search quality sign-off

The architecture is defense-in-depth by design. The reference implementation is not a substitute for those enterprise controls.
