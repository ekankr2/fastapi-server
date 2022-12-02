from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.routers.router import api_router

app = FastAPI(
    title='FastAPI Server',
)


app.include_router(api_router, prefix=settings.API_PREFIX)
