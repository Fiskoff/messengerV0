from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvLoader:
    load_dotenv()


class DatabaseENV(EnvLoader):
    DB_USER: str = getenv("DB_USER")
    DB_PASSWORD: str = getenv("DB_PASSWORD")
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: str = getenv("DB_PORT")
    DB_NAME: str = getenv("DB_NAME")


class ServerENV(EnvLoader):
    SERVER_HOST: str = getenv("SERVER_HOST")
    SERVER_PORT: int = int(getenv("SERVER_PORT"))


class RunConfig(BaseModel):
    host: str = ServerENV.SERVER_HOST
    port: int = ServerENV.SERVER_PORT


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DataBaseConfig(BaseModel):
    url: str = f"postgresql+asyncpg://{DatabaseENV.DB_USER}:{DatabaseENV.DB_PASSWORD}@{DatabaseENV.DB_HOST}:{DatabaseENV.DB_PORT}/{DatabaseENV.DB_NAME}"
    echo: bool = True
    pool_size: int = 10
    max_overflow: int = 15


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig = DataBaseConfig()


settings = Settings()