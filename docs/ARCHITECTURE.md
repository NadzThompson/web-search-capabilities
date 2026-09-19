# Architecture

## Query plane

```text
User / NOVA Orchestrator
        |
        v
Search Security Gateway
  - proprietary classification
  - content-type detection
  - DLP / secrets / PII
  - ALLOW / TRANSFORM / BLOCK
        |
        v
NOVA Internal Search Index
  - Elastic/BM25
  - PGVector semantic retrieval
  - Evidence metadata
        |
        v
Treasury Reranker
        |
        v
Evidence Validator
        |
        v
Synthesis Model
        |
        v
Output DLP / policy
        |
        v
User
```

## Crawl plane

```text
Public Internet
    |
    v
Controlled Crawler
  - robots policy
  - allow/block source policy
  - DNS/IP validation
  - SSRF protection
  - redirect validation
  - content-size/type limits
    |
    v
Untrusted Content Boundary
    |
    v
Prompt Injection Firewall
  - active-content stripping
  - hidden-content removal
  - malicious instruction detection
  - encoded instruction heuristics
  - quarantine
    |
    v
ADLS Raw / Parsed / Quarantine
    |
    v
Databricks Enrichment
  - parsing
  - metadata
  - source classification
  - dedupe/versioning
  - entities
  - embeddings
    |
    +--> Elastic
    +--> PGVector
    +--> Graph / GraphRAG
```

## Key separation

The crawler reaches public websites. The user query does not have to. This lets NOVA support broad public-web research while minimizing query-data leakage.
