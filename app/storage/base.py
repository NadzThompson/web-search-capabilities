from abc import ABC, abstractmethod

class EvidenceStore(ABC):
    @abstractmethod
    async def put_raw(self, key: str, data: bytes, content_type: str) -> str: ...
    @abstractmethod
    async def put_text(self, key: str, text: str) -> str: ...
