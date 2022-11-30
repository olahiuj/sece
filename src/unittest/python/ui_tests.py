import unittest

from problem import *
from diff import *
from ui import *

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


def test_program_pair(filename1, filename2):
    prog1 = Program(f"{UNITTEST_FOLDER_PATH}/../input/{filename1}")
    prog2 = Program(f"{UNITTEST_FOLDER_PATH}/../input/{filename2}")
    diff_parser = DiffParser(prog1, prog2)
    diff_result = diff_parser.parse_diff()
    ui_ = UI()
    ui_.update_text(diff_result, prog1.get_path(), prog2.get_path())
    ui_.main_loop()


class SimpleUITest(unittest.TestCase):
    def test_single_program_pair_diff_display(self):
        test_program_pair("4A/127473352.cpp", "4A/134841308.cpp")
        test_program_pair("4A/84822638.cpp", "4A/84822639.cpp")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
