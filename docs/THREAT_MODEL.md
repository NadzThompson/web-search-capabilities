# STRIDE-style Threat Summary

- **Spoofing:** malicious domain impersonates trusted publisher. Control with canonical-domain registry, TLS and provenance metadata.
- **Tampering:** retrieved/indexed content altered. Control with SHA-256 hashes, versioning, immutable raw evidence and restricted write identities.
- **Repudiation:** untraceable search/index actions. Control with request IDs and append-oriented audit/SIEM events.
- **Information disclosure:** proprietary query/log/tool leakage. Control with DLP, abstraction, deny-by-default egress, log minimization and output DLP.
- **Denial of service:** huge pages/crawl loops. Control with byte/time/depth/concurrency/rate limits.
- **Elevation of privilege:** prompt injection/tool abuse. Control with content-as-data boundary, least privilege, policy validation, sandboxing and network isolation.
