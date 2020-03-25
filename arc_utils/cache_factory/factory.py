# factory.py

from enum import Enum
from .cache import Cache
from .redis import Redis


class Caches(Enum):
    REDIS = "redis"


class CacheFactory:

    @staticmethod
    def get(name: str,url,retries) -> Cache:
        if name == Caches.REDIS.value:
            return Redis(url,retries)

        raise NotImplemented(f"{name} cache not implemented yet")

