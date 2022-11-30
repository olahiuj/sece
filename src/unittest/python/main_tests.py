import os
import sys
import unittest

from main import main

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class SimpleMainTest(unittest.TestCase):
    def test_input(self):
        sys.argv = ["sece", "auto", f"{UNITTEST_FOLDER_PATH}/../input/", "/tmp/output/"]
        result = main()
        # only checks folder count
        self.assertEqual(
            2,
            len(result)
        )


if __name__ == '__main__':
    unittest.main()
