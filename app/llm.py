import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(prompt: str) -> str:
    response = requests.post(
        RENDER_API_URL,
        json={"prompt": prompt}
    )
    return response.json()["response"]