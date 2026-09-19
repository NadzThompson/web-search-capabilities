from app.ranking.scorer import score
from app.skills.types import SkillResult

def run(chunks: list, jurisdiction: str | None = None, top_k: int = 10) -> SkillResult:
    ranked = [score(c, jurisdiction) for c in chunks]
    ranked.sort(key=lambda c: c.final_score, reverse=True)
    return SkillResult(True, {'chunks': ranked[:top_k]})
