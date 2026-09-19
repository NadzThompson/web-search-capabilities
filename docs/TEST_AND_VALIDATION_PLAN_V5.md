# Test and Validation Plan v5

## Unit tests
Test all 16 skills independently, including invalid/empty inputs and fail-closed behaviour.

## LangGraph tests
- correct agent routing;
- mixed-query decomposition;
- blocked search terminates;
- insufficient evidence loops only through approved retrieval paths;
- mandatory security nodes cannot be skipped;
- state carries classification, policy, source, and audit metadata.

## Data leakage tests
- Restricted/Sensitive/Confidential/Internal data in body, URL, headers, metadata;
- encoded proprietary data;
- alternate-language proprietary data;
- credentials, tokens, customer PII, payment data;
- attempts to instruct the agent to bypass DLP;
- canary tokens must never appear outside approved boundary.

Target: zero restricted/credential/customer-data leakage.

## Prompt-injection tests
- direct user injection;
- webpage indirect injection;
- PDFs and document metadata;
- hidden CSS/HTML;
- base64/encoded instructions;
- malicious links/tool requests;
- citation manipulation;
- source telling agent to ignore regulators;
- memory/index poisoning attempts.

Target: zero unauthorized tool execution/exfiltration.

## Search quality tests
Measure:
- authoritative recall@k;
- citation precision;
- claim support rate;
- freshness accuracy;
- jurisdiction accuracy;
- source diversity;
- evidence-sufficiency calibration;
- latency and cost.

## Performance
Separate indexed-search SLA from live-fetch SLA. Live crawl/fetch is not the default critical path when fresh indexed evidence exists.
