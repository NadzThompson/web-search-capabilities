from app.security.output_dlp import check_output
from app.skills.types import SkillResult

def run(text: str) -> SkillResult:
    result = check_output(text)
    return SkillResult(result.allowed, {'safe': result.allowed, 'findings': result.findings, 'text': text if result.allowed else None}, errors=[] if result.allowed else ['output_dlp_block'])
