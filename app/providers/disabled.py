from .base import ExternalSearchProvider
class DisabledProvider(ExternalSearchProvider):
    name = "disabled"
    async def search(self, query: str, top_k: int):
        return []
