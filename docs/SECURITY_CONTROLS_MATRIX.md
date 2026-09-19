# Security Controls Matrix

| Threat | Prevent | Detect | Respond |
|---|---|---|---|
| Proprietary query leakage | classification, DLP, transform/block, network gateway | audit hash, egress logs, canaries | block, alert, investigate |
| Secrets/credentials | deterministic scanner, Key Vault, no prompt secrets | DLP/SIEM | hard block, rotate if exposed |
| Direct prompt injection | non-overridable policy engine | policy events | deny request |
| Indirect prompt injection | sanitize, quarantine, least privilege | injection signals | quarantine/source downgrade |
| SSRF | DNS/IP validation, redirect checks, egress firewall | proxy/firewall telemetry | block domain/IP |
| Malicious documents | size/type controls, sandbox integration | malware scanner | quarantine |
| Citation/source poisoning | trust tiers, provenance, corroboration | source-diversity and contradiction checks | downgrade/remove source |
| Index poisoning | quarantine before indexing, content hashes | anomaly/version monitoring | purge affected versions |
| Log leakage | hash/minimize queries | log scanning | redact/purge and investigate |
| Tool abuse | least privilege, policy validation | tool audit | deny/revoke identity |
