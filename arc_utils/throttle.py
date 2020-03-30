import time
from functools import partial, wraps


class TooSoon(Exception):
    """Can't be called so soon"""
    pass


class CoolDownDecorator(object):
    def __init__(self, func, interval):
        self.func = func
        self.interval = interval
        self.last_run_for_user = {}
        self.user_id_key = "user_id"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return partial(self, obj)

    def __call__(self, *args, **kwargs):

        now = time.time()
        user_id = args[0][self.user_id_key]

        if user_id not in self.last_run_for_user:
            self.last_run_for_user[user_id] = now
            return self.func(*args, **kwargs)

        if (now - self.last_run_for_user[user_id]) < self.interval:
            raise TooSoon()

        else:
            self.last_run_for_user[user_id] = now
            return self.func(*args, **kwargs)

class CoolDownNotificationDecorator(object):
    def __init__(self, func, interval):
        self.func = func
        self.interval = interval
        self.last_run_for_user = {}
        self.user_name = "username"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return partial(self, obj)

    def __call__(self, *args, **kwargs):

        now = time.time()
        user_id = args[0][self.user_name]

        if user_id not in self.last_run_for_user:
            self.last_run_for_user[user_id] = now
            return self.func(*args, **kwargs)

        if (now - self.last_run_for_user[user_id]) < self.interval:
            raise TooSoon()

        else:
            self.last_run_for_user[user_id] = now
            return self.func(*args, **kwargs)


def NotificationThrottle(interval):
    def applyDecorator(func):
        decorator = CoolDownNotificationDecorator(func=func, interval=interval)
        return wraps(func)(decorator)

    return applyDecorator
def LogThrottle(interval):
    def applyDecorator(func):
        decorator = CoolDownDecorator(func=func, interval=interval)
        return wraps(func)(decorator)

    return applyDecorator
