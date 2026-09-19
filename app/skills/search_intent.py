from __future__ import annotations
from enum import StrEnum
from app.skills.types import SkillResult

class SearchIntent(StrEnum):
    REGULATORY = 'regulatory'
    MACRO = 'macroeconomic'
    COMPANY = 'company'
    MARKETS = 'markets'
    RESEARCH = 'research'
    INNOVATION = 'innovation'
    OPEN_WEB = 'open_web'

KEYWORDS = {
    SearchIntent.REGULATORY: {'osfi','basel','regulation','guideline','rule','capital','lcr','nsfr'},
    SearchIntent.MACRO: {'gdp','inflation','cpi','unemployment','central bank','rate decision','macro'},
    SearchIntent.COMPANY: {'company','earnings','investor relations','annual report','10-k','10-q'},
    SearchIntent.MARKETS: {'market','yield','spread','bond','fx','equity','volatility','repo'},
    SearchIntent.RESEARCH: {'paper','research','study','academic','working paper'},
    SearchIntent.INNOVATION: {'ai','technology','fintech','tokenized','innovation','agentic'},
}

def run(query: str) -> SkillResult:
    q = query.lower()
    scored = [(intent, sum(1 for k in kws if k in q)) for intent, kws in KEYWORDS.items()]
    intent, score = max(scored, key=lambda x: x[1], default=(SearchIntent.OPEN_WEB, 0))
    if score == 0:
        intent = SearchIntent.OPEN_WEB
    return SkillResult(True, {'intent': intent.value, 'confidence': min(1.0, 0.5 + score * 0.15)})
