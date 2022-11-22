import os
from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    ENVIRONMENT: str = os.getenv('ENVIRONMENT')
    DB_URL: str = os.getenv('DB_URL')

    class Config:
        env_file = ".env.local"


settings = Settings()