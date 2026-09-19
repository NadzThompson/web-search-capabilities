from enum import StrEnum

class Classification(StrEnum):
    RESTRICTED = "restricted"
    SENSITIVE = "sensitive"
    CONFIDENTIAL = "confidential"
    INTERNAL = "internal"
    PUBLIC = "public"

CLASSIFICATION_SEVERITY = {
    Classification.PUBLIC: 0,
    Classification.INTERNAL: 1,
    Classification.CONFIDENTIAL: 2,
    Classification.SENSITIVE: 3,
    Classification.RESTRICTED: 4,
}

class ContentType(StrEnum):
    CLIENT = "client"
    COUNTERPARTY = "counterparty"
    TRANSACTION = "transaction"
    POSITION = "position"
    BALANCE = "balance"
    EXPOSURE = "exposure"
    FORECAST = "forecast"
    EMPLOYEE_PII = "employee_pii"
    CUSTOMER_PII = "customer_pii"
    CREDENTIAL = "credential"
    SECRET = "secret"
    PROPRIETARY_MODEL = "proprietary_model"
    INTERNAL_PROJECT = "internal_project"
    PAYMENT_DATA = "payment_data"
    AUTH_DATA = "authentication_data"

class Decision(StrEnum):
    ALLOW = "allow"
    TRANSFORM = "transform"
    BLOCK = "block"

class SearchMode(StrEnum):
    STRICT = "strict"
    TRUSTED = "trusted"
    OPEN = "open"

class SourceTier(StrEnum):
    T1_PRIMARY = "t1_primary"
    T2_INSTITUTIONAL = "t2_institutional"
    T3_ESTABLISHED = "t3_established"
    T4_COMMENTARY = "t4_commentary"
    T5_GENERAL = "t5_general"
    T6_UNVERIFIED = "t6_unverified"
