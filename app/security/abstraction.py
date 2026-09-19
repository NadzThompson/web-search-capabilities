import re

_REPLACEMENTS = [
    (re.compile(r"[$€£]\s?\d+(?:\.\d+)?\s?(?:bn|mm|million|billion)?", re.I), ""),
    (re.compile(r"\b\d+(?:\.\d+)?\s?(?:bn|mm|million|billion)\b", re.I), ""),
    (re.compile(r"(?i)\b(our|we|us|my|current internal|actual)\b"), ""),
    (re.compile(r"(?i)\bRBC\b"), "bank"),
    (re.compile(r"(?i)\bNOVA\b"), "treasury platform"),
]

def abstract_query(text: str) -> str:
    out = text
    for pattern, repl in _REPLACEMENTS:
        out = pattern.sub(repl, out)
    out = re.sub(r"\s+", " ", out).strip(" ,;:-")
    # Prefer external/public research concepts over internal scenario wording.
    if len(out) < 8:
        return "financial regulation and treasury risk public information"
    return out
