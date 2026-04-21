from fastapi import APIRouter, Depends, HTTPException

simulate_router = APIRouter(
    prefix="/api",
    tags=["simulate"],
    responses={404: {"description": "Not found"}},
)

@simulate_router.get("/")
async def simulate():
    return {"message": "This is a simulation endpoint."}