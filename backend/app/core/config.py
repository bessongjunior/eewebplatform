import os
from typing import ClassVar

from pydantic_settings import BaseSettings



class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DATABASE_HOSTNAME: str = 'postgres'
    DATABASE_PORT: int = 5432
    DATABASE_PASSWORD: str = 'eelimited12hannahtabetando'
    DATABASE_NAME: str = 'eelimited_db'
    DATABASE_USERNAME: str = 'root' #postgres
    # WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    # READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # SENTRY_SDN: str|None = None
    SENTRY_SDN: ClassVar[None] = None
    CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    DATABASE_HOSTNAME: str = 'postgres'
    DATABASE_PORT: int = 5432
    DATABASE_PASSWORD: str = 'eelimited12hannahtabetando'
    DATABASE_NAME: str = 'eelimited_db'
    DATABASE_USERNAME: str = 'root' #postgres
    # WRITER_DB_URL: str = f"mysql+aiomysql://root:fastapi@db:3306/fastapi"
    # READER_DB_URL: str = f"mysql+aiomysql://root:fastapi@db:3306/fastapi"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    DATABASE_PORT: int = 5432
    DATABASE_PASSWORD: str = 'eelimited12hannahtabetando'
    DATABASE_NAME: str = 'eelimited_db'
    DATABASE_USERNAME: str = 'root' #postgres
    # WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    # READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"


class ProductionConfig(Config):
    DATABASE_HOSTNAME: str = 'postgres'
    DATABASE_PORT: int = 5432
    DATABASE_PASSWORD: str = 'eelimited12hannahtabetando'
    DATABASE_NAME: str = 'eelimited_db'
    DATABASE_USERNAME: str = 'root'
    # WRITER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/prod"
    # READER_DB_URL: str = f"mysql+aiomysql://fastapi:fastapi@localhost:3306/prod"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()

