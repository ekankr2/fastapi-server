import os
from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
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

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DATABASE_USERNAME"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=values.get("DATABASE_PORT"),
            path=f"/{values.get('DATABASE_NAME') or ''}",
        )

    class Config:
        env_file = ".env.local"


settings = Settings()