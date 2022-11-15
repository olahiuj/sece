import dataclasses

from checker import Checker
from generator import Input, Char, Int, String, GeneratorRAND
from program import *


@dataclasses.dataclass
class ProblemResult:
    equal_pairs: List[Tuple[str, str]]
    inequal_pairs: List[Tuple[str, str]]


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


class Problem:
    """a subfolder of the input folder

    This class represents exactly one subfolder under the input
    folder. Equivalence of all programs in one Problem should 
    be checked.
    """

    def __init__(self, folder: str) -> None:
        self.__folder__ = folder
        self.__programs__ = []
        self.__stdin_format__ = []
        for file in os.listdir(folder):
            abs_file_path = folder + file
            if file.endswith(".c") or file.endswith(".cpp"):
                self.__programs__.append(Program(abs_file_path))
            elif file == "stdin_format.txt":
                with open(abs_file_path) as fp:
                    self.__stdin_format__ = fp.readlines()

        if not self.__stdin_format__:
            raise RuntimeError("stdin_format.txt not found")

    @cache
    def programs(self) -> List[Program]:
        return self.__programs__

    @cache
    def get_input_format(self) -> Input:
        return Parser.parse(''.join(self.__stdin_format__))

    @cache
    def get_folder(self) -> str:
        return self.__folder__

    def solve(self) -> ProblemResult:
        eq, neq = [], []
        programs = self.programs()
        for i1 in range(len(programs)):
            for i2 in range(i1):
                p1, p2 = programs[i1], programs[i2]
                stdin = self.get_input_format()
                g = GeneratorRAND(stdin)
                if Checker.check(p1, p2, g):
                    eq.append((p1.get_path(), p2.get_path()))
                else:
                    neq.append((p1.get_path(), p2.get_path()))

        return ProblemResult(eq, neq)
