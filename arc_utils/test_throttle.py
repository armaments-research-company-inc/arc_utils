import unittest
import time

from .throttle import LogThrottle, TooSoon
@LogThrottle(1)
def hello(log):
    return log["id"]

@LogThrottle(1)
def testTwo_hello(log):
    return log["id"]

@LogThrottle(1)
def testThree_hello(log):
    return log["id"]


@LogThrottle(1)
def testFour_hello(log):
    return log["id"]

class TestThrottle(unittest.TestCase):
    def testThrottle_ShouldRaiseTooSoonException(self):
        try:
            hello({"id":1})
            out = hello({"id": 1})
            self.assertEqual(out, 1)
        except Exception as e:
            self.assertIsInstance(e, TooSoon)

    def testThrottle_ShouldReturnDataForDifferentId(self):
        try:
            x = testTwo_hello({"id": 1})
            y = testTwo_hello({"id": 2})
            self.assertEqual(x, 1)
            self.assertEqual(y, 2)

        except Exception as e:
            self.assertEqual(True, False)

    def testThrottle_ShouldReturnDataAfterInterval(self):
        try:
            x = testThree_hello({"id": 1})
            self.assertEqual(x, 1)
            time.sleep(1)
            y = testThree_hello({"id": 1})
            self.assertEqual(x, 1)
        except Exception as e:
            self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
