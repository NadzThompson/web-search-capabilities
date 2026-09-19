import re
from app.evidence.citation_verifier import verify_claim_against_chunk
from app.skills.types import SkillResult

def run(claim: str, chunk) -> SkillResult:
    terms = {t for t in re.findall(r'[A-Za-z0-9%.-]+', claim.lower()) if len(t) > 2}
    check = verify_claim_against_chunk(terms, chunk)
    return SkillResult(check.supported, {'supported': check.supported, 'reason': check.reason}, errors=[] if check.supported else ['claim_not_supported'])
