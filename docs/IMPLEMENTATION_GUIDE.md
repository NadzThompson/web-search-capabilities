# Implementation Guide

## 1. Build the query-security boundary first

Deploy the Search Security Gateway before enabling crawling or any external-provider fallback. Integrate enterprise DLP/classification. Validate that raw Restricted/Sensitive/Confidential/Internal prompts cannot leave through query strings, request bodies, URLs, headers or logs.

## 2. Build the internal search index

Create Elastic/OpenSearch lexical indices and PGVector semantic tables. Use `sql/elastic_mapping.json` and `sql/pgvector_schema.sql` as starting points. Keep source metadata and immutable hashes with every chunk.

## 3. Create ADLS evidence zones

Use managed identity and private networking. Store raw bytes before parsing. Quarantine suspicious content separately and do not publish it to retrieval indices.

## 4. Deploy the crawler separately

The crawler should have controlled outbound access; the search API should not require arbitrary Internet egress. Enforce DNS/IP validation and redirect checks independently of model behavior.

## 5. Connect Databricks

Use Databricks for asynchronous parsing/enrichment/embeddings. Do not make synchronous Databricks jobs part of normal user-query latency.

## 6. Add prompt-injection and malware controls

Use deterministic sanitization plus bank-approved document security controls. Do not depend on an LLM classifier alone. High-risk content is quarantined before indexing.

## 7. Add hybrid retrieval and reranking

Retrieve from lexical and semantic indices, fuse results, then apply source authority, primary-source, freshness, jurisdiction and corroboration features. Search engine ranking is never evidence authority.

## 8. Add synthesis as a separate trust boundary

Provide the synthesis model only with approved evidence chunks. External content is data, not instructions. Run claim/citation verification and output DLP before delivery.

## 9. Operationalize

Add SIEM alerts, source registry governance, crawl SLOs, stale-source alerts, index versioning, disaster recovery, canary leakage tests and continuous prompt-injection red-teaming.
