from __future__ import annotations
from typing import Any, TypedDict
from app.models.schemas import EvidenceChunk

class WebSearchState(TypedDict, total=False):
    request_id: str
    original_query: str
    safe_query: str
    classification: str
    content_types: list[str]
    policy_decision: str
    intent: str
    search_mode: str
    planned_queries: list[str]
    jurisdiction: str | None
    evidence: list[EvidenceChunk]
    warnings: list[str]
    prompt_injection_flags: list[str]
    evidence_sufficient: bool
    final_answer: str
    blocked_reason: str
    audit_events: list[dict[str, Any]]
