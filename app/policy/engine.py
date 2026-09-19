from app.models.enums import Classification, ContentType, Decision
from app.models.schemas import ClassificationResult, GatewayResult
from app.security.abstraction import abstract_query
from app.security.dlp import scan

_ALWAYS_BLOCK_TYPES = {
    ContentType.CREDENTIAL,
    ContentType.SECRET,
    ContentType.AUTH_DATA,
    ContentType.CUSTOMER_PII,
    ContentType.PAYMENT_DATA,
}

def decide(query: str, classification: ClassificationResult) -> GatewayResult:
    findings = scan(query)
    if any(f.severity == "critical" for f in findings):
        return GatewayResult(decision=Decision.BLOCK, original_classification=classification, blocked_reason="critical_dlp_finding")
    if classification.classification == Classification.RESTRICTED or _ALWAYS_BLOCK_TYPES.intersection(classification.content_types):
        return GatewayResult(decision=Decision.BLOCK, original_classification=classification, blocked_reason="restricted_or_prohibited_content")
    if classification.classification in {Classification.SENSITIVE, Classification.CONFIDENTIAL, Classification.INTERNAL}:
        return GatewayResult(decision=Decision.TRANSFORM, original_classification=classification, safe_query=abstract_query(query))
    return GatewayResult(decision=Decision.ALLOW, original_classification=classification, safe_query=query)
