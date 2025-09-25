from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import PlainTextResponse
from .agents.retriever import retrieve_answer
from .agents.summarizer import summarize
from .agents.escalation import escalate
from .analytics.logger import log_interaction

app = FastAPI(title="AI Support Agent", version="0.1.0")

class AskRequest(BaseModel):
    user_id: str
    message: str

REQS = Counter('requests_total', 'Total /ask requests')
RESOLVED = Counter('resolved_total', 'Resolved via FAQ')
ESCALATED = Counter('escalated_total', 'Escalated to human')

@app.post("/ask")
def ask(req: AskRequest):
    REQS.inc()
    answer, conf = retrieve_answer(req.message)
    if conf >= 0.85:
        RESOLVED.inc()
        final = summarize(answer)
        log_interaction(req.user_id, req.message, final, route="faq", resolved=True)
        return {"answer": final, "route": "faq", "confidence": conf}
    else:
        ESCALATED.inc()
        final = escalate(req.user_id, req.message)
        log_interaction(req.user_id, req.message, final, route="escalated", resolved=False)
        return {"answer": final, "route": "escalated", "confidence": conf}

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}
