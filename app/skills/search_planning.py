from app.skills.types import SkillResult

def run(query: str, intent: str, jurisdiction: str | None = None) -> SkillResult:
    plans = [query.strip()]
    if jurisdiction:
        plans.append(f'{query.strip()} {jurisdiction}')
    if intent == 'regulatory':
        plans.append(f'{query.strip()} official regulator primary source')
    elif intent == 'macroeconomic':
        plans.append(f'{query.strip()} official statistics central bank')
    elif intent == 'company':
        plans.append(f'{query.strip()} investor relations filing')
    elif intent in {'innovation','research'}:
        plans.append(f'{query.strip()} research industry commentary')
    dedup = list(dict.fromkeys(p for p in plans if p))
    return SkillResult(True, {'queries': dedup[:5]})
