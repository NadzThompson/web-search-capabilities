# ADLS and Databricks Integration

## ADLS Gen2 role

ADLS is the evidence system of record for retrieved public content. Keep original bytes and immutable hashes so an answer can be reconstructed later.

Suggested zones:

```text
web-evidence/
  raw/
  parsed/
  quarantine/
  evidence/
  versions/
```

Use managed identity / workload identity. Avoid embedded storage keys.

## Databricks role

Databricks handles asynchronous large-scale processing:

- PDF/document parsing orchestration
- metadata extraction
- source classification
- deduplication/version comparison
- entity extraction
- chunking
- embedding generation through approved endpoints
- Delta lineage tables
- publication to Elastic/PGVector/Graph

The API/search path should not depend on Databricks completing a job synchronously for every user query. Pre-processing keeps latency low.
