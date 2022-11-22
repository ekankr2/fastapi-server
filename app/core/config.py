import os
from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    ENVIRONMENT: str = os.getenv('ENVIRONMENT')
    DB_URL: str = os.getenv('DB_URL')
    API_PREFIX: str = os.getenv('API_PREFIX')
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_PORT: str = os.getenv('DATABASE_PORT')
    DATABASE_USERNAME: str = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    JWT_SECRET_ACCESS_KEY: str = os.getenv('JWT_SECRET_ACCESS_KEY')
    JWT_SECRET_REFRESH_KEY: str = os.getenv('JWT_SECRET_REFRESH_KEY')

    class Config:
        env_file = ".env.local"


settings = Settings()