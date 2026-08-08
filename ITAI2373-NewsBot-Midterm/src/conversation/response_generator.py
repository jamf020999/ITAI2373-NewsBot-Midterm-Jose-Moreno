"""Small response helpers for the conversational interface."""
def response_message(intent, count=None):
    if intent == "search":
        return f"Found {count or 0} relevant articles."
    if intent == "entities":
        return "Top named entities are shown below."
    if intent == "topics":
        return "The discovered topics are shown below."
    return None
