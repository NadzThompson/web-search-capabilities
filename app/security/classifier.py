import re
from app.models.enums import Classification, ContentType, CLASSIFICATION_SEVERITY
from app.models.schemas import ClassificationResult

_PATTERNS: list[tuple[ContentType, re.Pattern[str]]] = [
    (ContentType.CREDENTIAL, re.compile(r"(?i)(api[_ -]?key|client[_ -]?secret|password|bearer\s+[a-z0-9._-]+)")),
    (ContentType.AUTH_DATA, re.compile(r"(?i)(access[_ -]?token|refresh[_ -]?token|private[_ -]?key|ssh-rsa)")),
    (ContentType.CUSTOMER_PII, re.compile(r"(?i)(sin\b|social insurance|date of birth|customer id|account number)")),
    (ContentType.EMPLOYEE_PII, re.compile(r"(?i)(employee id|staff id|payroll|home address)")),
    (ContentType.COUNTERPARTY, re.compile(r"(?i)\bcounterpart(y|ies)\b")),
    (ContentType.TRANSACTION, re.compile(r"(?i)\b(transaction|trade id|deal id|ticket)\b")),
    (ContentType.POSITION, re.compile(r"(?i)\b(position|inventory|holdings?)\b")),
    (ContentType.BALANCE, re.compile(r"(?i)\b(balance|deposit base|liquidity buffer)\b")),
    (ContentType.EXPOSURE, re.compile(r"(?i)\b(exposure|limit utilization|concentration)\b")),
    (ContentType.FORECAST, re.compile(r"(?i)\b(forecast|projection|outlook assumption)\b")),
    (ContentType.INTERNAL_PROJECT, re.compile(r"(?i)\b(NOVA|internal project|codename)\b")),
]

_EXPLICIT_LABELS = {
    "restricted": Classification.RESTRICTED,
    "sensitive": Classification.SENSITIVE,
    "confidential": Classification.CONFIDENTIAL,
    "internal": Classification.INTERNAL,
    "public": Classification.PUBLIC,
}

_DEFAULT_BY_TYPE = {
    ContentType.CREDENTIAL: Classification.RESTRICTED,
    ContentType.SECRET: Classification.RESTRICTED,
    ContentType.AUTH_DATA: Classification.RESTRICTED,
    ContentType.CUSTOMER_PII: Classification.RESTRICTED,
    ContentType.PAYMENT_DATA: Classification.RESTRICTED,
    ContentType.EMPLOYEE_PII: Classification.SENSITIVE,
    ContentType.CLIENT: Classification.SENSITIVE,
    ContentType.COUNTERPARTY: Classification.SENSITIVE,
    ContentType.TRANSACTION: Classification.SENSITIVE,
    ContentType.POSITION: Classification.SENSITIVE,
    ContentType.BALANCE: Classification.SENSITIVE,
    ContentType.EXPOSURE: Classification.SENSITIVE,
    ContentType.FORECAST: Classification.CONFIDENTIAL,
    ContentType.PROPRIETARY_MODEL: Classification.CONFIDENTIAL,
    ContentType.INTERNAL_PROJECT: Classification.INTERNAL,
}

def classify(text: str) -> ClassificationResult:
    lower = text.lower()
    found: list[ContentType] = []
    reasons: list[str] = []
    level = Classification.PUBLIC

    for label, enum_value in _EXPLICIT_LABELS.items():
        if re.search(rf"(?i)\b{re.escape(label)}\b", text):
            if CLASSIFICATION_SEVERITY[enum_value] > CLASSIFICATION_SEVERITY[level]:
                level = enum_value
                reasons.append(f"explicit_{label}_label")

    for content_type, pattern in _PATTERNS:
        if pattern.search(text):
            found.append(content_type)
            candidate = _DEFAULT_BY_TYPE.get(content_type, Classification.INTERNAL)
            if CLASSIFICATION_SEVERITY[candidate] > CLASSIFICATION_SEVERITY[level]:
                level = candidate
            reasons.append(f"detected_{content_type.value}")

    # monetary amounts combined with first-party terms indicate proprietary context
    if re.search(r"(?i)\b(our|we|current|actual)\b", text) and re.search(r"[$€£]\s?\d|\b\d+(?:\.\d+)?\s?(?:bn|mm|million|billion)\b", lower):
        if CLASSIFICATION_SEVERITY[Classification.SENSITIVE] > CLASSIFICATION_SEVERITY[level]:
            level = Classification.SENSITIVE
        reasons.append("first_party_financial_amount")

    return ClassificationResult(classification=level, content_types=sorted(set(found), key=lambda x: x.value), reasons=reasons or ["no_proprietary_signal"])
