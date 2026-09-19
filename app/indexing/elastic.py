from .base import SearchIndex
from app.config import settings
from app.models.schemas import EvidenceChunk

class ElasticIndex(SearchIndex):
    def __init__(self):
        if not settings.nova_elastic_url:
            raise RuntimeError("NOVA_ELASTIC_URL is required")
        from elasticsearch import AsyncElasticsearch
        self.client = AsyncElasticsearch(settings.nova_elastic_url)
        self.index = settings.nova_elastic_index
    async def upsert(self, chunks: list[EvidenceChunk]) -> None:
        from elasticsearch.helpers import async_bulk
        actions = [{"_index": self.index, "_id": c.chunk_id, "_source": c.model_dump(mode="json")} for c in chunks]
        await async_bulk(self.client, actions)
    async def search(self, query: str, top_k: int) -> list[EvidenceChunk]:
        resp = await self.client.search(index=self.index, size=top_k, query={"multi_match":{"query":query,"fields":["text^3","source.title^2","source.domain"]}})
        out=[]
        for hit in resp["hits"]["hits"]:
            c=EvidenceChunk.model_validate(hit["_source"])
            c.lexical_score=float(hit.get("_score") or 0)
            out.append(c)
        return out
