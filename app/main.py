from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import simulate
from app.dependencies import get_query_token
from app.api.v1.endpoints import ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulate.simulate_router, dependencies=[Depends(get_query_token)])
app.include_router(ai.router, dependencies=[Depends(get_query_token)])

@app.get("/")
async def root():
    return {"message": "Hello World"}