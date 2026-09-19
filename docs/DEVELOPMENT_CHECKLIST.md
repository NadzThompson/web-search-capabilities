# Development Checklist

## Foundation
- [ ] Create repo and protected branches
- [ ] Configure CI/CD and artifact registry
- [ ] Create DEV/TEST/UAT/PROD identities
- [ ] Configure secrets through Key Vault

## Security Gateway
- [ ] Integrate enterprise classification hierarchy
- [ ] Integrate DLP/PII/secrets services
- [ ] Confirm raw non-public query egress is denied
- [ ] Confirm fail-closed behavior
- [ ] Add URL/header/body/log channel tests

## Crawler
- [ ] Dedicated identity/runtime
- [ ] Azure Firewall/proxy rules
- [ ] robots/rate/depth limits
- [ ] SSRF/redirect controls
- [ ] malware/document sandbox
- [ ] quarantine storage

## Storage and processing
- [ ] ADLS zones
- [ ] Delta/Unity Catalog tables
- [ ] Databricks parsing/enrichment jobs
- [ ] content hashes and versions
- [ ] retention/legal hold rules

## Retrieval
- [ ] Elastic lexical index
- [ ] PGVector semantic index
- [ ] approved embeddings
- [ ] hybrid fusion
- [ ] Treasury ranking
- [ ] source modes STRICT/TRUSTED/OPEN

## Evidence and synthesis
- [ ] evidence provenance
- [ ] claim/citation verifier
- [ ] prompt-injection boundary
- [ ] output DLP
- [ ] insufficient-evidence behavior

## Validation
- [ ] unit/integration tests
- [ ] 500+ Treasury gold set
- [ ] prompt-injection red team
- [ ] canary leakage tests
- [ ] penetration test
- [ ] load/latency/SLO tests
- [ ] DR/rollback tests

## Governance
- [ ] Security approval
- [ ] Privacy approval
- [ ] Architecture approval
- [ ] Model Validation approval
- [ ] source licensing/terms review
- [ ] production operational ownership
