# Test and Validation Plan

## Functional

- search modes and filtering
- source ranking
- freshness and jurisdiction
- crawl/index/update/version flow
- citation/evidence metadata

## Security

- Restricted blocking
- Sensitive/Confidential/Internal raw-egress prevention
- secrets and credentials
- customer/employee PII
- URLs, headers, query strings and log channels
- direct prompt injection
- indirect webpage/PDF injection
- hidden text
- encoded payloads
- malicious redirects
- SSRF: localhost, RFC1918, link-local, metadata IPs, IPv6 local ranges
- oversized responses
- unsupported content types
- source/index poisoning

## Canary leakage

Place synthetic markers such as `NOVA_TEST_SECRET_<id>` in test queries and verify they never appear in proxy/provider/firewall logs beyond the gateway.

## Quality benchmark

Maintain a 500+ question Treasury gold set spanning liquidity, capital, ALM, funding, macro, company research, regulation, market infrastructure and current news.

Metrics: authoritative recall@k, citation precision, claim support, freshness accuracy, jurisdiction accuracy, source diversity, unsafe leakage rate, injection execution rate, latency and cost/query.

Targets for prohibited leakage and unauthorized tool execution should be zero.
