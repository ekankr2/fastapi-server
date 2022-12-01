from fastapi import FastAPI
from app.core.config import settings
from app.routers.router import api_router

app = FastAPI(
    title='FastAPI-server',
)

app.include_router(api_router, prefix=settings.API_PREFIX)
