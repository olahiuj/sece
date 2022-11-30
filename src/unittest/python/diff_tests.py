import unittest

from problem import *
from diff import *

UNITTEST_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))


class DiffTest(unittest.TestCase):
    def test_single_program_pair_diff(self):
        prog1 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/127473352.cpp")
        prog2 = Program(f"{UNITTEST_FOLDER_PATH}/../input/4A/134841308.cpp")
        diff_parser = DiffParser(prog1, prog2)
        diff_result = diff_parser.parse_diff()
        self.assertEqual(
            [{
                'line': '#include <iostream>',
                'type': 'D',
                'left_diff': [8], 'right_diff': [],
                'newline': '#include<iostream>'
            }, {
                'line': 'using namespace std; ',
                'type': 'D',
                'left_diff': [20], 'right_diff': [],
                'newline': 'using namespace std;'
            }, {
                'line': 'int main() {',
                'type': 'D',
                'left_diff': [10], 'right_diff': [],
                'newline': 'int main(){'
            }, {
                'line': '\tcout<<"YES";',
                'type': 'S'
            }, {
                'line': '\treturn 0;',
                'type': 'S'
            }, {
                'line': '}',
                'type': 'L'
            }, {
                'line': '} ',
                'type': 'R'
            }],
            list(diff_result)
        )

    def test_another_single_program_pair_diff(self):
        prog1 = Program(f"{UNITTEST_FOLDER_PATH}/../input/50A/21508887.cpp")
        prog2 = Program(f"{UNITTEST_FOLDER_PATH}/../input/50A/21508898.cpp")
        diff_parser = DiffParser(prog1, prog2)
        diff_result = diff_parser.parse_diff()
        self.assertEqual(
            [{
                'line': '#include <iostream>',
                'type': 'S'
            }, {
                'line': 'main(){long long n,m;std::cin>>n>>m;std::clog<<m*n/2;}',
                'type': 'D',
                'left_diff': [7, 8, 10, 11, 12, 13, 14, 15], 'right_diff': [7, 9],
                'newline': 'main(){int n,m;std::cin>>n>>m;std::clog<<m*n/2;}'
            }],
            list(diff_result)
        )


if __name__ == '__main__':
    unittest.main()
