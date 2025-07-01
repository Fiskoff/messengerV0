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


class JwtENV(EnvLoader):
    JWT_SECRET_KEY: str = getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(getenv("REFRESH_TOKEN_EXPIRE_DAYS"))


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


class JWTConfig(JwtENV):
    secret_key: str = JwtENV.JWT_SECRET_KEY
    algorithm: str = JwtENV.JWT_ALGORITHM
    access_expire: str = JwtENV.ACCESS_TOKEN_EXPIRE_MINUTES
    refresh_expire: str = JwtENV.REFRESH_TOKEN_EXPIRE_DAYS


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig = DataBaseConfig()
    jwt: JWTConfig = JWTConfig()


settings = Settings()