from abc import ABC, abstractmethod
from app.models.schemas import EvidenceChunk

class ExternalSearchProvider(ABC):
    name: str
    @abstractmethod
    async def search(self, query: str, top_k: int) -> list[EvidenceChunk]: ...
