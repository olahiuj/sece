from typing import *

from generator import Input, Char, Int, String


class ParserException(Exception):
    def __init__(self, message: str):
        super(self).__init__(message)


class Parser:
    """stdin_format.txt parser

    This is the parser that parses stdin_format.txt and returns
    a list of lines. Each line contains a list of Data.
    """

    @staticmethod
    def parse(stdin_format: str) -> Input:
        result = []
        for line in stdin_format.strip().split('\n'):
            line_result = []
            for token in line.strip().split():
                if token[0] == 'i':
                    (l, r) = token.split(',')
                    line_result.append(Int(int(l.removeprefix('int(')), int(r.removesuffix(')'))))
                elif token[0] == 's':
                    (l, r) = token.split(',')
                    line_result.append(String(int(l.removeprefix('string(')), int(r.removesuffix(')'))))
                elif token[0] == 'c':
                    line_result.append(Char())
                else:
                    raise ParserException(f"unknown token: {token}")
            result.append(line_result)
        return result


class Program:
    """one program source code

    This is the internal representation of source program found
    in each subfolder of the input folder.
    """

    def __init__(self, path: str) -> None:
        pass

    def run(self, input_file_path: str) -> Tuple[str, int]:
        """run this program and generate (stdout, exit code)

        Args:
            input_file_path (str): path to generated input file

        Returns:
            Tuple[str, int]: stdout and exit code
        """
        pass


class Problem:
    """a subfolder of the input folder

    This class represents exactly one subfolder under the input
    folder. Equivalence of all programs in one Problem should 
    be checked.
    """

    def __init__(self, folder: str) -> None:
        pass

    def programs(self) -> List[Program]:
        pass

    def get_input_format(self) -> Input:
        pass
