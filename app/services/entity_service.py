import json
import re

from app.utils.hf_client import hf_text

def _parse_entity_array(raw_text: str) -> list[str]:
    text = raw_text.strip()

    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if str(item).strip()]
    except json.JSONDecodeError:
        pass

    match = re.search(r"\[[\s\S]*\]", text)
    if not match:
        return []

    try:
        parsed = json.loads(match.group(0))
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if str(item).strip()]
    except json.JSONDecodeError:
        return []

    return []


def generate_entities(model_response: str) -> list[str]:
    formatted_prompt = (
        "Extract important entities from the scenario.\n\n"
        "Return strictly in this format:\n"
        "[\"entity1\", \"entity2\"]\n\n"
        f"Sentence: {model_response}"
    )
    raw_output = hf_text(formatted_prompt)
    return _parse_entity_array(raw_output)