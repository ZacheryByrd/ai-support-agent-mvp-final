def summarize(text: str) -> str:
    # Placeholder: in real use, call an LLM or heuristic summarizer.
    if len(text) > 320:
        return text[:300] + "..."
    return text
