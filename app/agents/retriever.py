import json, re
from pathlib import Path
from typing import Tuple

FAQ_PATH = Path(__file__).parent.parent / "data" / "faqs.json"
_FAQS = json.loads(FAQ_PATH.read_text())

def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())

def retrieve_answer(question: str) -> Tuple[str, float]:
    q = normalize(question)
    # Exact match
    if q in _FAQS:
        return _FAQS[q], 0.99
    # Fuzzy: keyword containment
    for k, v in _FAQS.items():
        if all(word in q for word in k.split()[:3]):
            return v, 0.7
    return "", 0.0
