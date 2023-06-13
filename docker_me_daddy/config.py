__all__ = ['settings']

from pydantic.env_settings import BaseSettings
from pydantic.networks import PostgresDsn, RedisDsn


class Settings(BaseSettings):
    SOME: str = "OOPS! Unset:("
    POSTGRES: PostgresDsn = 'postgresql+psycopg://username:password@hostname:5432/database'
    REDIS: RedisDsn = 'redis://username:password@hostname:6379/0'

    class Config:
        env_prefix = "DOCKER_ME_DADDY_"
        env_file = ".env"


settings = Settings()