import unittest

from problem import *

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class SimpleCheckerTest(unittest.TestCase):
    def test_YES_yes(self):
        p1 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/127473352.cpp")
        p2 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/101036360.cpp")
        self.assertEqual(
            False,
            Checker.check(p1, p2, GeneratorRAND([[Int(1, 100)]]))
        )

    def test_YES_YES(self):
        p1 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/127473352.cpp")
        p2 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/134841308.cpp")
        self.assertEqual(
            True,
            Checker.check(p1, p2, GeneratorRAND([[Int(1, 100)]]))
        )


if __name__ == '__main__':
    unittest.main()
