import re
from dataclasses import dataclass

@dataclass(frozen=True)
class DLPFinding:
    rule: str
    severity: str
    match: str

_RULES = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "secret_assignment": re.compile(r"(?i)\b(api[_-]?key|client[_-]?secret|password|token)\s*[:=]\s*\S+"),
    "bearer": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]+=*"),
    "long_number": re.compile(r"\b\d{10,19}\b"),
}

def scan(text: str) -> list[DLPFinding]:
    findings: list[DLPFinding] = []
    for name, pattern in _RULES.items():
        for m in pattern.finditer(text):
            severity = "critical" if name in {"secret_assignment", "bearer"} else "high"
            findings.append(DLPFinding(name, severity, m.group(0)[:80]))
    return findings
