from ..slack.client import post_message

def escalate(user_id: str, question: str):
    # Post to Slack (if configured) or simply mark as escalated
    text = f":rotating_light: Escalation from {user_id}: {question}"
    post_message(text)
    return "Thanks! I couldn't confidently answer that. A human agent will follow up shortly."
