from app.skills.types import SkillResult


def reciprocal_rank_fusion(result_lists: list[list], k: int = 60) -> list:
    scores = {}
    objects = {}
    for results in result_lists:
        for rank, item in enumerate(results, 1):
            key = getattr(item, 'chunk_id', None) or repr(item)
            objects[key] = item
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
    return [objects[key] for key, _ in sorted(scores.items(), key=lambda x: x[1], reverse=True)]

async def run(query: str, lexical_index, semantic_index=None, top_k: int = 10) -> SkillResult:
    lexical = await lexical_index.search(query, top_k)
    semantic = await semantic_index.search(query, top_k) if semantic_index else []
    fused = reciprocal_rank_fusion([lexical, semantic])[:top_k]
    return SkillResult(True, {'chunks': fused, 'lexical_count': len(lexical), 'semantic_count': len(semantic)})
