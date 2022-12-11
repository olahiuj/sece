import unittest
import sys
import os
import tempfile

from main import main

INTEGRATION_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with tempfile.TemporaryDirectory() as output_dir:
            sys.argv = [
                './sece',
                'manual',
                f"{INTEGRATION_FOLDER_PATH}/../input",
                output_dir
            ]
            result = main()
            mapped_result = list(map(
                lambda x: len(x.equal_pairs) + len(x.inequal_pairs),
                result
            ))
            total_len = sum(mapped_result)
            print(total_len)
            print(mapped_result)
            self.assertEqual(total_len, 94)


if __name__ == '__main__':
    unittest.main()
