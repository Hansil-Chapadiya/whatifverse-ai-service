import requests
import os

API_URL = os.getenv("MODEL_API_URL")
DEFAULT_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

def hf_text(prompt: str) -> str:
    api_key = os.getenv("HF_API_KEY")
    if not api_key:
        raise ValueError("HF_API_KEY environment variable not set")

    model = os.getenv("HF_MODEL", DEFAULT_MODEL)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
    }

    res = requests.post(API_URL, headers=headers, json=payload, timeout=45)
    if not res.ok:
        raise RuntimeError(f"HF API error {res.status_code}: {res.text}")

    data = res.json()
    return data["choices"][0]["message"]["content"]