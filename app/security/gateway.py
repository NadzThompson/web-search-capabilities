from app.models.schemas import GatewayResult
from .classifier import classify
from app.policy.engine import decide

def evaluate(query: str) -> GatewayResult:
    result = classify(query)
    return decide(query, result)
