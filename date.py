# date.py

import time
from datetime import datetime

class DateUtils():

    def __init__(self, refTime=datetime(2016, 1, 1, 0, 0, 0)):
        self.refTime = refTime
        self.milliseconds = 1000

    def elapsed_time(self) -> int:
        now = datetime.utcnow()
        elapsed = (now - self.refTime).total_seconds()
        return elapsed * self.milliseconds


    def elapsed_from(self, time_in_ms) -> int:
        return self.elapsed_time() - time_in_ms