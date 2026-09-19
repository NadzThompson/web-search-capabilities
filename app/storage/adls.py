from .base import EvidenceStore
from app.config import settings

class ADLSEvidenceStore(EvidenceStore):
    """Azure Blob/ADLS adapter. Uses DefaultAzureCredential; no secrets in code."""
    def __init__(self):
        if not settings.nova_adls_account_url:
            raise RuntimeError("NOVA_ADLS_ACCOUNT_URL is required")
        from azure.identity.aio import DefaultAzureCredential
        from azure.storage.blob.aio import BlobServiceClient
        self._credential = DefaultAzureCredential()
        self._service = BlobServiceClient(settings.nova_adls_account_url, credential=self._credential)
        self._container = self._service.get_container_client(settings.nova_adls_container)
    async def put_raw(self, key: str, data: bytes, content_type: str) -> str:
        name = f"raw/{key}"
        await self._container.upload_blob(name, data, overwrite=True, content_type=content_type)
        return name
    async def put_text(self, key: str, text: str) -> str:
        name = f"parsed/{key}"
        await self._container.upload_blob(name, text.encode(), overwrite=True, content_type="text/plain")
        return name
