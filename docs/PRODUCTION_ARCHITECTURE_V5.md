# NOVA Web Search Production Architecture v5

## Logical architecture

```text
                        NOVA USER
                            |
                            v
                  LANGGRAPH ORCHESTRATOR
                            |
       +--------------------+--------------------+
       |                    |                    |
       v                    v                    v
Treasury Navigator    Risk Calculator     Scenario Simulator
                            |
                            +--------------------+
                                                 |
                                                 v
                                        WEB SEARCH AGENT
                                                 |
                                                 v
                                    SEARCH SECURITY GATEWAY
                          +----------------------+------------------+
                          | classification / DLP / entity labels   |
                          | query abstraction / policy / audit     |
                          +----------------------+------------------+
                                                 |
                                         SAFE QUERY ONLY
                                                 |
                    +----------------------------+-----------------------+
                    |                                                    |
                    v                                                    v
             NOVA SEARCH INDEX                                  TARGETED CRAWL
      Elastic/BM25 + PGVector + Graph                                |
                    |                                           SSRF / robots
                    |                                                |
                    |                                     Prompt Injection Firewall
                    |                                                |
                    +----------------------------+-------------------+
                                                 v
                                          SAFE EVIDENCE
                                                 |
                                        Evidence Reranking
                                                 |
                                          Corroboration
                                                 |
                                      Evidence Sufficiency
                                                 |
                                      Citation Verification
                                                 |
                                         Evidence Synthesis
                                                 |
                                            Output DLP
                                                 |
                                                 v
                                             LANGGRAPH
                                                 |
                                                 v
                                               USER
```

## Crawl/data plane

```text
Public Web -> Safe Crawler -> Untrusted Content -> Injection/Malware Controls
          -> ADLS raw/parsed/quarantine/evidence/version zones
          -> Databricks parse/enrich/deduplicate/embed/entity extraction
          -> Elastic + PGVector + Graph
```

## Core security principle
Protect the query without unnecessarily restricting the user's ability to research. Public-source breadth and proprietary-data egress are separate policy concerns.
