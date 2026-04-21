from fastapi import APIRouter, HTTPException
from app.services.ai_service import generate_text
from app.services.entity_service import generate_entities
from app.schemas.ai import (
    EntitiesRequest,
    EntitiesResponse,
    GenerateRequest,
    GenerateResponse,
)

router = APIRouter(
    prefix="/api/v1/ai",
    tags=["ai"],
    responses={404: {"description": "Not found"}},
)

@router.post("/generate", response_model=GenerateResponse)
async def generate(payload: GenerateRequest):
    try:
        result = generate_text(payload.prompt)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"generated_text": result}

@router.post("/entities", response_model=EntitiesResponse)
async def extract_entities(payload: EntitiesRequest):
    try:
        result = generate_entities(payload.model_response)
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"entities": result}