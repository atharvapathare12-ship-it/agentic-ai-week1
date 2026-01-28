def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Memory state:", memory)

    if len(memory["steps"]) == 0:
        return "call_llm"

    memory["completed"] = True
    return "stop"
