from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory

def run_agent(goal: str):
    print("\n[AGENT] Starting agent")
    memory = init_memory(goal)

    while True:
        print("\n[AGENT] Loop iteration started")

        step = decide_next_step(memory)
        print("[AGENT] Control returned step:", step)

        if step == "call_llm":
            print("[AGENT] Executing LLM step")
            response = call_llm(goal)

            memory["steps"].append(response)
            print("[AGENT] Memory updated, steps count:", len(memory["steps"]))

        elif step == "stop":
            print("[AGENT] STOP received → breaking loop")
            break

    print("[AGENT] Agent stopped cleanly")
