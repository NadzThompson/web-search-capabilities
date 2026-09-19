from app.skills.types import SkillResult

async def run(query: str, index, top_k: int = 10, external_provider=None) -> SkillResult:
    chunks = await index.search(query, top_k)
    used_external = False
    if not chunks and external_provider is not None:
        chunks = await external_provider.search(query, top_k)
        used_external = True
    return SkillResult(True, {'chunks': chunks, 'used_external_provider': used_external})
