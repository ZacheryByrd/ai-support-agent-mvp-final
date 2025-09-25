# AI-Powered Customer Support Agent (MVP)

A production-lean, **multi-agent** customer support service that can:
- Answer FAQs (retrieval agent)
- Summarize and format responses (summarizer agent)
- **Escalate** unclear cases (escalation agent)
- Log **analytics** to SQLite and expose **/metrics** for Prometheus

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d '{
  "user_id": "u123",
  "message": "What is your return policy?"
}'
```

## ENV

Copy `.env.example` to `.env` and fill as needed.

## Deploy (Docker)

```bash
docker build -t ai-support-agent:dev .
docker run -p 8000:8000 --env-file .env ai-support-agent:dev
```

## Notes

- Lightweight analytics in `app/analytics/log.db` (created at runtime).
- Prometheus metrics at `/metrics`.
- Slack integration is stubbed; wire your webhook in `.env`.
