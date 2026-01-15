def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)

    if memory["completed"]:
        print("[CONTROL] completed=True → STOP")
        return "stop"

    if len(memory["steps"]) == 0:
        print("[CONTROL] No steps yet → CALL LLM")
        return "call_llm"

    print("[CONTROL] Steps exist → Mark completed and STOP")
    memory["completed"] = True
    return "stop"
