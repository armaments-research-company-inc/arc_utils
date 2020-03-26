# __init__.py

import time
import redis

from arc_utils.cache_factory import cache


class Redis(cache.Cache):

    def __init__(self,url,max_retries):

        self.redis_client = redis.StrictRedis.from_url(url)
        self.max_retries=max_retries
        self.retriesLeft = max_retries
        self.waitTime = 1
        self.accumulatingFactor = 1.2   # seconds

    def __retry(function):
        def wrapper(*args, **kwargs):

            self = args[0]
            while self.retriesLeft:
                try:
                    result = function(*args, **kwargs)
                    self.retriesLeft = self.max_retries
                    self.waitTime = 1
                    return result
                except redis.ConnectionError:
                    print(f're-establishing connection with redis... retries left {self.retriesLeft}')
                    self.retriesLeft -= 1
                    time.sleep(self.waitTime)
                    self.waitTime *= self.accumulatingFactor

            raise redis.ConnectionError()
        return wrapper

    @__retry
    def set(self, name, value) -> bool:
        return self.redis_client.set(name, value)

    @__retry
    def get(self, name) -> bytes:
        return self.redis_client.get(name)

    @__retry
    def expire(self, token, time):
        return self.redis_client.expire(token, time)

    @__retry
    def delete(self, name):
        return self.redis_client.delete(name)