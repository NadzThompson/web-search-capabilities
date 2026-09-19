def chunk_text(text: str, max_chars: int = 1800, overlap: int = 200) -> list[str]:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return [text] if text else []
    out = []
    start = 0
    while start < len(text):
        end=min(len(text), start+max_chars)
        out.append(text[start:end])
        if end == len(text):
            break
        start=max(0, end-overlap)
    return out
