# Crawling and Source Governance

## Search universe

NOVA should be broad about public information while being strict about outbound proprietary data. Recommended source categories include regulators, central banks, governments, supranationals, banks, companies, investor relations, exchanges, market infrastructure, macro/statistical sources, academic institutions, consultancies, financial media, vendors, specialist blogs and broader public-web sources.

## Search modes

- **STRICT**: primary and institutional sources.
- **TRUSTED**: adds established market/research/commentary sources.
- **OPEN**: broad public web; low-trust sources require corroboration and lower ranking.

## Source registry

Each domain should carry metadata such as publisher, trust tier, jurisdiction, primary-source flag, crawl frequency, allowed paths, disallowed paths, robots policy, parser type, retention class and licensing notes.

## Recommended crawl model

Pre-crawl high-value sources on a schedule. Use live targeted retrieval only when indexed evidence is missing or stale. This keeps most user searches low-latency.

## Storage lifecycle

- `raw/`: exact retrieved bytes and content hash
- `parsed/`: sanitized extracted content
- `quarantine/`: suspicious or unsafe content
- `evidence/`: validated evidence artifacts
- `versions/`: superseded versions and hashes

## Legal/operational controls

Respect robots.txt, source terms, copyright/licensing, rate limits, retention requirements and source-specific access restrictions. Do not bypass authentication or anti-bot controls.
