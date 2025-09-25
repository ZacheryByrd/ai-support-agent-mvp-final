import os, json, urllib.request

WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "")

def post_message(text: str) -> bool:
    if not WEBHOOK:
        return False  # Not configured in MVP
    body = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(WEBHOOK, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as _:
            return True
    except Exception:
        return False
