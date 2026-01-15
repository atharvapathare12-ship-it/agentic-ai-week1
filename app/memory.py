def init_memory(goal: str) -> dict:
    memory = {
        "goal": goal,
        "steps": [],
        "completed": False
    }
    print("[MEMORY] Initialized:", memory)
    return memory