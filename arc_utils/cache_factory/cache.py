# cache.py

from abc import ABC


class Cache(ABC):
    @classmethod
    def set(cls, key: str, value: str):
        pass

    @classmethod
    def get(cls, key: str):
        pass

    @classmethod
    def expire(self, token, time):
        pass

    @classmethod
    def delete(self, name):
        pass