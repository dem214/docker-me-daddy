from contextlib import suppress
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from docker_me_daddy.engine import get_session
from docker_me_daddy.redis import get_redis
from docker_me_daddy.config import settings

app = FastAPI()

@app.get("/")
def root():
    return "Hello, World!"

@app.get("/some/")
def some():
    return {"SOME_env_is": settings.SOME}

@app.get("/healthcheck")
async def healthcheck(
        redis: Annotated[Redis, Depends(get_redis)],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    is_redis = False
    is_postgres = False

    try:
        response: bool = await redis.ping()
        is_redis = response
    except Exception as exc:
        print(exc)

    try:
        result = await session.scalar(text("SELECT 1;"))
        is_postgres = result == 1
    except Exception as exc:
        print(exc)

    status_code = status.HTTP_200_OK if is_redis and is_postgres else status.HTTP_500_INTERNAL_SERVER_ERROR
    return JSONResponse(
        content={'redis': is_redis, 'postgres': is_postgres},
        status_code=status_code,
    )


def run(port: int = 8000, log_level: str =  "info"):
    uvicorn.run("main:app", port=port, log_level=log_level)

if __name__ == "__main__":
    run()
