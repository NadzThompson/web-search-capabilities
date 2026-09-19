from dataclasses import dataclass
from app.models.schemas import EvidenceChunk

@dataclass(frozen=True)
class CitationCheck:
    supported: bool
    reason: str


def verify_claim_against_chunk(claim_terms: set[str], chunk: EvidenceChunk) -> CitationCheck:
    """Reference lexical support check. Production should use an approved NLI/entailment model plus deterministic checks."""
    if not claim_terms:
        return CitationCheck(False, "empty_claim")
    text_terms = set(chunk.text.lower().split())
    overlap = len({t.lower() for t in claim_terms} & text_terms) / max(1, len(claim_terms))
    return CitationCheck(overlap >= 0.5, f"term_overlap={overlap:.2f}")
