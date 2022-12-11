import unittest

from generator import Int, Char, String
from problem import parse


class ParserTest(unittest.TestCase):
    def test_parse_int(self):
        self.assertEqual(
            [[Int(114, 514)]],
            parse("   int(114,514)  ")
        )

    def test_parse_char(self):
        self.assertEqual(
            [[Char()]],
            parse("   char  ")
        )

    def test_parse_string(self):
        self.assertEqual(
            [[String(114, 514)]],
            parse("   string(114,514)  ")
        )

    def test_parse_complex(self):
        self.assertEqual(
            [
                [Int(114, 514), String(233, 233), Char(), Char(), Int(22, 33)],
                [Char(), String(55, 66), Int(5, 6), Int(6, 6)]
            ],
            parse(
                """
                int(114,514) string(233,233) char  char int(22,33)
                char string(55,66) int(5,6) int(6,6)
                """)
        )


if __name__ == '__main__':
    unittest.main()
