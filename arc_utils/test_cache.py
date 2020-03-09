
import unittest
from .cache import FireArmCache
import time

class MockRedis:
    def get(self, key):
        return b'{"hello": "hello"}'

    def new_get(self, key):
        return b'{"hello": "v2"}'



class EmptyMockRedis:
    def get(self, key):
        return None


class TestFirearmCache(unittest.TestCase):
    def testCache_BeforeExpire(self):

        mr = MockRedis()
        fc = FireArmCache(mr, expire_time=1)
        firearm = fc.get_firearm_type("hello")

        self.assertEqual(firearm["hello"], "hello")
        mr.get  = mr.new_get
        firearm = fc.get_firearm_type("hello")
        self.assertEqual(firearm["hello"], "hello")

    def testCache_AfterExpire(self):

        mr = MockRedis()
        fc = FireArmCache(mr, expire_time=1)
        firearm = fc.get_firearm_type("hello")

        self.assertEqual(firearm["hello"], "hello")
        mr.get  = mr.new_get
        time.sleep(2)
        firearm = fc.get_firearm_type("hello")
        self.assertEqual(firearm["hello"], "v2")

    def testCache_DataFromRedisIsEmpty(self):

        mr = EmptyMockRedis()

        fc = FireArmCache(mr, expire_time=1)
        firearm = fc.get_firearm_type("1")

        self.assertEqual(firearm, None)



if __name__ == "__main__":
    unittest.main()
