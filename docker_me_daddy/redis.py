__all__ = ['get_redis']

from redis.asyncio import Redis

from .config import settings


def get_redis(url: str = settings.REDIS) -> Redis:
    return Redis.from_url(url)
