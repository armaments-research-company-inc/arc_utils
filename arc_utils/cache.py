import redis
import datetime
import json



class FireArmCache:
    """
    Wrapper to handle Caching for Firearm Types

    uni
    t of expire_time is seconds
    """
    def __init__(self, redis, expire_time=3):
        self.r = redis
        self.cache = dict()
        self.dataKey = "firearm"
        self.expiresInKey = "expires_in"
        self.expireTime = expire_time

    def __is_key_valid(self, expireTime):
        return (expireTime - datetime.datetime.utcnow()).total_seconds() > 0

    """
    get_firearm_type

    returns a firearm type against a firearm type id

    if firearm is not present in the local cache it fetches updated from redis
    """
    def get_firearm_type(self, key):

        if key in self.cache:

            expireTime = self.cache[key][self.expiresInKey]
            if self.__is_key_valid(expireTime):
                return json.loads(self.cache[key][self.dataKey])

        firearm = self.r.get(key)
        if firearm is None or firearm is "":
            return None

        delta = datetime.timedelta(0, self.expireTime)

        self.cache[key] = {
            self.expiresInKey: datetime.datetime.utcnow() + delta,
            self.dataKey: firearm,
        }

        return json.loads(firearm)
