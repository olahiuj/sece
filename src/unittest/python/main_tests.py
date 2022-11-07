import os
import unittest

from main import main

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class SimpleMainTest(unittest.TestCase):
    def test_input(self):
        result = main(f"{UNITTEST_FOLDER_PATH}/../input/")
        # only checks folder count
        self.assertEqual(
            2,
            len(result)
        )


if __name__ == '__main__':
    unittest.main()
