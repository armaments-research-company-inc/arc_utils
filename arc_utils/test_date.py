# test_date.py

import unittest
from datetime import datetime
import time
from .date import DateUtils


class TestDateUtils(unittest.TestCase):
    def testElapsedTime(self):

        dutils = DateUtils()
        from1970 = time.time() * 1000
        diff = from1970 - dutils.elapsed_time()
        years_elapsed = int(diff * 3.17098e-11)

        self.assertEqual(years_elapsed, 46, msg="years elapsed should be 46")

    def testElapsedFrom(self):
        dutils = DateUtils()

        from_time = datetime(2016, 1, 1, 1, 0)
        now = (datetime.utcnow() - from_time).total_seconds() * 1000
        diff = dutils.elapsed_from(now)
        self.assertEqual(int(diff / (3.6e6)), 1)


if __name__ == "__main__":
    unittest.main()
