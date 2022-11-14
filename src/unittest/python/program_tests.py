import os.path
import unittest

from problem import *

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class ProgramTest(unittest.TestCase):
    def test_single_program_run(self):
        prog = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/127473352.cpp")
        self.assertEqual(
            (b"YES", SUCCESS()),
            prog.run(tempfile.TemporaryFile())
        )
        self.assertEqual(
            "127473352.cpp",
            os.path.basename(prog.get_path())
        )


if __name__ == '__main__':
    unittest.main()
