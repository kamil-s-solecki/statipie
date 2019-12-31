import unittest
from statipie.request import Request


class RequestTest(unittest.TestCase):
    def test_init(self):
        r = Request(b'\x01')

        self.assertNotEqual(None, r)
