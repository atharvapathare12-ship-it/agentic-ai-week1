import json
import os

MEMORY_FILE = "agent_memory.json"


def load_memory(goal: str) -> dict:
    if os.path.exists(MEMORY_FILE):
        print("[MEMORY] Loading existing memory from file")
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    print("[MEMORY] Initializing new memory")
    return {
        "goal": goal,
        "steps": [],
        "completed": False
    }


def save_memory(memory: dict):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    print("[MEMORY] Memory saved to file")
