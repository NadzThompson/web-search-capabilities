# Prompt Injection Threat Model

All external HTML, PDFs, XML, RSS, blogs, filings and metadata are untrusted data.

## Attack classes

- Direct user injection: attempts to override search security policy.
- Indirect injection: malicious instructions embedded in retrieved web content.
- Hidden injection: CSS-hidden, metadata, comments or encoded instructions.
- Tool injection: content asking the model to call URLs/tools or exfiltrate data.
- Citation manipulation: content instructing NOVA to suppress or prefer sources.
- Memory poisoning: malicious content persisted into the index for later retrieval.

## Controls

1. External content has no instruction authority.
2. Strip scripts/forms/iframes/objects/styles and common hidden elements.
3. Detect override/exfiltration/tool-use instruction patterns.
4. Quarantine high-risk pages before indexing.
5. Do not provide the web reader with internal Treasury data or privileged action tools.
6. Require policy validation for any tool call.
7. Restrict outbound network access independently of model behavior.
8. Validate source provenance and corroborate important claims.
9. Run output DLP before downstream delivery/export.
10. Continuously red-team new injection variants.
