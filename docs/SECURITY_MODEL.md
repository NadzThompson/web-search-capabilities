# Security Model

## Threats addressed

- Sensitive data leakage through search queries, URLs, headers, logs or tool arguments
- Direct and indirect prompt injection
- SSRF and cloud-metadata access
- Tool abuse / arbitrary network calls
- Malicious HTML / hidden text / active content
- Search/citation poisoning
- Memory/index poisoning
- Credential leakage
- Unsafe redirects
- Oversized/malicious document ingestion

## Proprietary hierarchy

Highest to lowest sensitivity:

1. Restricted
2. Sensitive
3. Confidential
4. Internal
5. Public

Content-type labels are separate. Example: `Sensitive + Counterparty + Exposure`.

## Egress defaults

| Classification | Raw outbound query | Default |
|---|---:|---|
| Restricted | Never | Block |
| Sensitive | Never | Transform or block |
| Confidential | Never | Transform or block |
| Internal | Never | Transform |
| Public | Allowed | Allow |

Credentials, secrets, authentication data, customer PII and payment data are always blocked by the reference policy.

## Defense in depth

No single prompt, classifier or LLM is trusted to protect NOVA. Production protection is layered across:

- deterministic classification/DLP
- enterprise classification/DLP integration
- query abstraction
- application policy engine
- network egress policy
- SSRF controls
- least-privilege identities/tools
- prompt-injection sanitization/quarantine
- sandboxed document parsing
- malware scanning
- evidence provenance and source ranking
- output DLP
- SIEM/audit telemetry
- red-team/canary testing

If a critical security dependency is unavailable or policy cannot be resolved, external egress must fail closed.
