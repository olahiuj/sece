import unittest

from generator import *


class TestRandomGenerator(unittest.TestCase):
    @staticmethod
    def all_satisfy(predicate: Callable, seq: Iterable) -> bool:
        for x in seq:
            if not predicate(x):
                return False
        return True

    def test_char(self):
        for ch in GeneratorRAND([[Char()]]).gen():
            self.assertTrue(ch.isalpha())

    def test_string(self):
        for s in GeneratorRAND([[String(114, 514)]]).gen():
            self.assertTrue(114 <= len(s) <= 514)

            for c in s:
                self.assertTrue(c.isalpha())

    def test_int(self):
        for i in GeneratorRAND([[Int(114, 514)]]).gen():
            self.assertTrue(114 <= int(i) <= 514)


if __name__ == '__main__':
    unittest.main()
