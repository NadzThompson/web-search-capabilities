# Security Model v5

## Threat classes
1. Proprietary data leakage.
2. Direct prompt injection.
3. Indirect prompt injection from web/PDF/metadata.
4. SSRF and private-network access.
5. Tool abuse and unauthorized actions.
6. Malicious files / active content.
7. Citation/source poisoning and SEO manipulation.
8. Memory/index poisoning.
9. Credential leakage.
10. Log/telemetry leakage.

## Defence in depth
- Classification + DLP before any outbound search.
- Query abstraction and reclassification.
- Network-level deny-by-default egress.
- Least-privilege Web Search Agent.
- SSRF/DNS/redirect validation.
- Prompt-injection screening and quarantine.
- Untrusted-evidence prompt boundary.
- Source trust scoring.
- Evidence sufficiency and citation verification.
- Output DLP.
- Safe audit logging and SIEM.
- Canary tests and red-team exercises.

## Proprietary hierarchy
Restricted > Sensitive > Confidential > Internal > Public.

## Content labels
Client, Counterparty, Transaction, Position, Balance, Exposure, Forecast, Employee PII, Customer PII, Credential, Secret, Proprietary Model, Internal Project, Payment Data, Authentication Data.

## Policy examples
- Restricted + any content type -> BLOCK.
- Sensitive + Counterparty -> raw egress denied; abstract only if policy permits and post-abstraction reclassification is safe.
- Confidential + Forecast -> transform or block based on policy.
- Internal + Internal Project -> transform to public-safe query.
- Public + public regulation topic -> allow subject to source/network policy.
