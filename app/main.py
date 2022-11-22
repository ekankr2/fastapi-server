from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title='FastAPI-server',
    root_path=settings.API_PREFIX
)


@app.get('/')
def index():
    return {'hello': 'world'}