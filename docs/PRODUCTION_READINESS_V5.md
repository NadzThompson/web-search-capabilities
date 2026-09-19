# Production Readiness v5

## Status
This repository is a production-oriented engineering baseline. It is not automatically approved for GSIB production. Enterprise controls and environment-specific integrations must be completed and independently validated.

## Required before production

### Identity and access
- Entra workload identity / managed identity.
- RBAC for crawler, indexer, query API, Databricks jobs, storage, and operators.
- No long-lived credentials in prompts, source code, notebooks, or environment files.

### Data protection
- Integrate bank-approved information classification and DLP.
- Enforce hierarchy: Restricted > Sensitive > Confidential > Internal > Public.
- Maintain content-type labels separately.
- Fail closed if classification/DLP is unavailable.
- Prohibit raw non-public query egress.
- Apply output DLP.

### Network security
- Only Search Gateway/crawler may have approved outbound Internet access.
- Deny direct Internet access from other agents by default.
- Enforce FQDN/proxy/firewall policy.
- Block loopback, private, link-local, reserved, and cloud metadata endpoints.
- Revalidate redirects and resolved IPs.

### Prompt-injection defence
- Treat all external content as untrusted data.
- Run deterministic + model/classifier-based injection detection.
- Strip active content and hidden elements.
- Sandbox document parsing.
- Quarantine suspicious sources.
- Prevent external content from authorizing tool calls.
- Red-team direct and indirect injections.

### Evidence quality
- Source registry and governance owner.
- STRICT/TRUSTED/OPEN policies.
- Primary-source preference for regulatory/official macro claims.
- Citation verification.
- Evidence sufficiency gate.
- Version and hash every source artifact.

### Storage/processing
- ADLS Gen2 zones with retention, encryption, legal-hold requirements.
- Databricks jobs separated from interactive query path.
- Production Elastic/PGVector deployment and backup strategy.
- Graph integration with lineage.

### Observability and audit
- SIEM integration.
- Safe logs with query hashing and no proprietary payload duplication.
- Prompt, agent, skill, policy, model, index, and source-version metadata in traces.
- Canary exfiltration tests.

### Validation
- 500+ Treasury benchmark queries.
- prompt injection attack suite;
- data leakage suite;
- source-quality and citation-precision testing;
- performance and failover testing;
- penetration testing;
- model validation / architecture / security / privacy approvals.

## Non-bypassable defence-in-depth invariant
No single classifier, prompt, detector, model, or LLM is trusted to protect NOVA. Security depends on multiple independent layers: DLP, deterministic policy, least privilege, network enforcement, prompt-injection controls, safe tooling, output controls, audit, and testing.
