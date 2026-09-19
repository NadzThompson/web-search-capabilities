from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field, HttpUrl
from .enums import Classification, ContentType, Decision, SearchMode, SourceTier

class SearchRequest(BaseModel):
    query: str = Field(min_length=2, max_length=4000)
    mode: SearchMode = SearchMode.TRUSTED
    jurisdiction: str | None = None
    freshness_hours: int | None = Field(default=None, ge=1, le=8760)
    top_k: int = Field(default=10, ge=1, le=50)
    allowed_domains: list[str] = []

class ClassificationResult(BaseModel):
    classification: Classification
    content_types: list[ContentType] = []
    reasons: list[str] = []
    confidence: float = Field(default=1.0, ge=0, le=1)

class GatewayResult(BaseModel):
    decision: Decision
    original_classification: ClassificationResult
    safe_query: str | None = None
    blocked_reason: str | None = None

class SourceMetadata(BaseModel):
    url: str
    domain: str
    title: str = ""
    publisher: str | None = None
    published_at: datetime | None = None
    retrieved_at: datetime
    tier: SourceTier = SourceTier.T6_UNVERIFIED
    jurisdiction: str | None = None
    primary_source: bool = False
    content_hash: str
    injection_risk: float = 0.0

class EvidenceChunk(BaseModel):
    source: SourceMetadata
    chunk_id: str
    text: str
    lexical_score: float = 0
    semantic_score: float = 0
    authority_score: float = 0
    freshness_score: float = 0
    jurisdiction_score: float = 0
    corroboration_score: float = 0
    final_score: float = 0

class SearchResponse(BaseModel):
    request_id: str
    decision: Decision
    safe_query: str | None
    evidence: list[EvidenceChunk] = []
    warnings: list[str] = []
    latency_ms: int

class CrawlRequest(BaseModel):
    url: HttpUrl
    force: bool = False

class CrawlResult(BaseModel):
    url: str
    status: str
    stored: bool
    quarantined: bool
    reason: str | None = None
    metadata: dict[str, Any] = {}
