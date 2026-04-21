from app.utils.hf_client import hf_text

def generate_text(prompt: str) -> str:
    formatted_prompt = (
        "Generate a creative and unique 'what-if' scenario based on the user's input.\n"
        "Keep it concise (3–5 lines), but include vivid details and variation.\n"
        "Make each response different in tone, setting, and outcome.\n\n"
        f"User prompt: {prompt}"
    )
    return hf_text(formatted_prompt)