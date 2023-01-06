from fastapi import FastAPI
from fastapi.logger import logger

from app.core.config import settings
from app.api.router import api_router
from app.tests.utils.logger import init_loggers

app = FastAPI(
    title='FastAPI Server',
)

@app.on_event('startup')
async def startup_event():
    init_loggers()
    logger.info('helloworld')
    logger.info('helloworld')
    logger.info('helloworld')
    logger.warning('warn')


app.include_router(api_router, prefix=settings.API_PREFIX)
