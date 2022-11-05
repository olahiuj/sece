import os
import unittest

from problem import Int
from problem import Problem

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class SimpleProblemTest(unittest.TestCase):
    def test_50A(self):
        prob = Problem(f"{UNITTEST_FOLDER_PATH}/../input/50A/")
        self.assertEqual(
            12,
            len(prob.programs())
        )
        self.assertEqual(
            [[Int(1, 16), Int(1, 16)]],
            prob.get_input_format()
        )
        self.assertEqual(
            "50A",
            os.path.basename(os.path.dirname(prob.get_folder()))
        )

    def test_4A(self):
        prob = Problem(f"{UNITTEST_FOLDER_PATH}/../input/4A/")
        self.assertEqual(
            8,
            len(prob.programs())
        )
        self.assertEqual(
            [[Int(1, 100)]],
            prob.get_input_format()
        )
        self.assertEqual(
            "4A",
            os.path.basename(os.path.dirname(prob.get_folder()))
        )


if __name__ == '__main__':
    unittest.main()
