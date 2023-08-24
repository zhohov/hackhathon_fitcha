from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_URl: str
    secret_key: str

    class Config:
        env_file = './.env'


settings = Settings()
