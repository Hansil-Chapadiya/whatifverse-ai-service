from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=3, max_length=2000)


class GenerateResponse(BaseModel):
    generated_text: str


class EntitiesRequest(BaseModel):
    model_response: str = Field(..., min_length=3, max_length=4000)


class EntitiesResponse(BaseModel):
    entities: list[str]
