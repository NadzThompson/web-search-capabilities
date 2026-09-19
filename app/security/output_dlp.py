from dataclasses import dataclass
from app.security.dlp import scan

@dataclass(frozen=True)
class OutputDLPResult:
    allowed: bool
    findings: list[str]


def check_output(text: str) -> OutputDLPResult:
    findings = scan(text)
    critical = [f.rule for f in findings if f.severity == "critical"]
    return OutputDLPResult(allowed=not critical, findings=[f.rule for f in findings])
