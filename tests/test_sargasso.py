import unittest
from sargasso import add

class TestSargasso(unittest.TestCase):
    def test_add(self):
        assert add(1, 2) == 3
