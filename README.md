# WhatIfVerse AI Service

FastAPI service that generates short **what-if scenarios** and extracts **important entities** from generated text using a Hugging Face model.

## Features
- Scenario generation (`/api/v1/ai/generate`)
- Entity extraction (`/api/v1/ai/entities`)
- Token-protected routes via header dependency
- `.env` loading at app startup

## Tech Stack
- FastAPI
- Pydantic v2
- Requests
- python-dotenv
- Uvicorn

## Project Structure
- `app/main.py` – app bootstrap, router registration, env loading
- `app/api/v1/endpoints/ai.py` – AI endpoints
- `app/services/ai_service.py` – scenario prompt formatting
- `app/services/entity_service.py` – entity prompt + parser
- `app/utils/hf_client.py` – Hugging Face HTTP client
- `app/schemas/ai.py` – request/response models

## Requirements
- Python 3.14+ (project currently uses `environment/` venv)
- Hugging Face API key

## Setup
1. Create/activate virtual environment (if not already active)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env` in project root with:

```env
HF_API_KEY=your_hf_token
MODEL_API_URL=https://router.huggingface.co/v1/chat/completions
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct
token=your_internal_token
```

## Run
```bash
uvicorn app.main:app --reload
```

Service starts at: `http://127.0.0.1:8000`

## Authentication Header
All included routers use dependency `get_query_token`, so send this header:

- Header name: `token`
- Header value: same value as `.env` `token`

## API

### 1) Generate scenario
`POST /api/v1/ai/generate`

Body:
```json
{
  "prompt": "What if humans were aliens?"
}
```

Response:
```json
{
  "generated_text": "..."
}
```

### 2) Extract entities
`POST /api/v1/ai/entities`

Body:
```json
{
  "model_response": "Generated scenario text here..."
}
```

Response:
```json
{
  "entities": ["Earth", "humans", "interstellar migration"]
}
```

## Quick cURL Examples
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ai/generate" \
  -H "Content-Type: application/json" \
  -H "token: your_internal_token" \
  -d '{"prompt":"What if humans were aliens?"}'
```

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ai/entities" \
  -H "Content-Type: application/json" \
  -H "token: your_internal_token" \
  -d '{"model_response":"Humans arrived on Earth from a distant star system..."}'
```

## Notes
- If `MODEL_API_URL` is missing, requests may fail in `hf_client.py`.
- If `HF_API_KEY` is missing/invalid, API returns upstream auth errors.
- Keep `.env` private; do not commit secrets.
