def decide_next_step(memory: dict) -> str:
    """
    Control flow decides what happens next.
    """
    if not memory["has_responded"]:
        return "call_llm"

    return "stop"
