# date.py

import time
from datetime import datetime, timedelta


class DateUtils:
    def __init__(
        self,
        updatedRefTime=datetime(2016, 1, 1, 0, 0, 0),
        defaultRefTime=datetime(1970, 1, 1, 0, 0, 0),
    ):
        self.updatedRefTime = updatedRefTime
        self.defaultRefTime = defaultRefTime
        self.milliseconds = 1000.0

    def elapsed_time(self) -> int:
        now = datetime.utcnow()
        elapsed = (now - self.updatedRefTime).total_seconds()
        return int(elapsed * self.milliseconds)

    def elapsed_from(self, time_in_ms) -> int:
        return int(self.elapsed_time() - time_in_ms)

    def calculate_no_of_days(self, updated_time_stamp, previous_timestamp):
        return str(updated_time_stamp - previous_timestamp).split(" ")[0]

    def calculate_timestamp(self, device_timestamp):
        days = int(self.calculate_no_of_days(self.updatedRefTime, self.defaultRefTime))
        delta = timedelta(days=days)
        dt = datetime.fromtimestamp(float(device_timestamp) / 1000.0)
        return dt + delta
