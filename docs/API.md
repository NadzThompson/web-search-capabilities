# API

## Health

`GET /health`

## Search

`POST /v1/search`

```json
{
  "query": "What is the current OSFI liquidity adequacy guideline?",
  "mode": "strict",
  "jurisdiction": "Canada",
  "top_k": 10
}
```

The response returns the gateway decision, safe query, ranked evidence, warnings and latency. Production synthesis should be a separate controlled step so retrieval and generation remain independently auditable.

## Crawl

`POST /v1/crawl`

```json
{"url":"https://www.osfi-bsif.gc.ca/..."}
```

Disabled by default. Enable only in an approved crawler runtime with controlled Internet egress.
