from typing import Any, Dict

class Message:
    def __init__(self, topic: str, payload: Dict[str, Any]):
        self.topic = topic
        self.payload = payload

class Bus:
    """A minimal in-process message bus (simulating MCP-style routing)."""
    def __init__(self):
        self.handlers = {}

    def subscribe(self, topic: str, handler):
        self.handlers.setdefault(topic, []).append(handler)

    async def publish(self, msg: Message):
        for handler in self.handlers.get(msg.topic, []):
            await handler(msg)
