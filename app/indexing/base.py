from abc import ABC, abstractmethod
from app.models.schemas import EvidenceChunk

class SearchIndex(ABC):
    @abstractmethod
    async def upsert(self, chunks: list[EvidenceChunk]) -> None: ...
    @abstractmethod
    async def search(self, query: str, top_k: int) -> list[EvidenceChunk]: ...
