from typing import Annotated
from fastapi import Header, HTTPException
import os

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: Annotated[str, Header()]):
    if token != os.getenv("token"):
        raise HTTPException(status_code=400, detail="No jessica token provided")