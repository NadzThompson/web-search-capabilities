import re
from .base import SearchIndex
from app.models.schemas import EvidenceChunk

class MemoryIndex(SearchIndex):
    def __init__(self):
        self.items: dict[str, EvidenceChunk] = {}
    async def upsert(self, chunks: list[EvidenceChunk]) -> None:
        for c in chunks:
            self.items[c.chunk_id] = c
    async def search(self, query: str, top_k: int) -> list[EvidenceChunk]:
        q = set(re.findall(r"\w+", query.lower()))
        scored = []
        for c in self.items.values():
            tokens = set(re.findall(r"\w+", c.text.lower()))
            lexical = len(q & tokens) / max(1, len(q))
            copy = c.model_copy(deep=True)
            copy.lexical_score = lexical
            scored.append(copy)
        return sorted(scored, key=lambda x: x.lexical_score, reverse=True)[:top_k]
