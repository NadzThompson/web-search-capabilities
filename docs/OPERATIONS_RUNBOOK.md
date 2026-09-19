# Operations Runbook

## Alerts

- unexpected increase in blocked/ transformed queries
- canary leakage event
- prompt-injection quarantine spike
- crawler error/redirect/SSRF spike
- stale Tier-1 sources
- indexing lag
- unusual source-domain growth
- audit/SIEM delivery failure

## Emergency controls

1. Set `NOVA_ALLOW_LIVE_FETCH=false`.
2. Disable optional external providers.
3. Revoke crawler workload identity outbound permissions.
4. Continue serving only the last approved internal index.
5. Quarantine affected content hashes and remove them from retrieval indices.

## Routine operations

- review new source-domain requests
- review quarantine samples
- compare regulator source hashes/versions
- monitor crawl freshness and index lag
- rotate/patch runtimes
- execute prompt-injection regression tests after model/parser changes
