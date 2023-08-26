from datetime import datetime
from typing import Any

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: Any
    REFRESH_TOKEN_EXPIRE_MINUTES: Any

    class Config:
        env_file = './.env'


settings = Settings()
