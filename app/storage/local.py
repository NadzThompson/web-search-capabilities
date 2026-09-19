from pathlib import Path
from .base import EvidenceStore

class LocalEvidenceStore(EvidenceStore):
    def __init__(self, root: str = ".data"):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
    async def put_raw(self, key: str, data: bytes, content_type: str) -> str:
        path = self.root / "raw" / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return str(path)
    async def put_text(self, key: str, text: str) -> str:
        path = self.root / "parsed" / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return str(path)
