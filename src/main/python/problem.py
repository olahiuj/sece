import dataclasses

import diff
import ui
from checker import Checker
from generator import Input, Char, Int, String, GeneratorRAND
from program import *
from closure import Closure

EQ, NEQ = False, False


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

    def solve(self, is_manual: bool) -> ProblemResult:
        neq, eq = [], []
        tr = Closure(set())
        programs: List[Program] = self.programs()
        for i1 in range(len(programs)):
            for i2 in range(i1):
                p1, p2 = programs[i1], programs[i2]
                if not tr.contains(p1, p2):
                    stdin = self.get_input_format()
                    g = GeneratorRAND(stdin)
                    if not Checker.check(p1, p2, g):
                        neq.append((p1.get_path(), p2.get_path()))
                    else:
                        if not is_manual:
                            eq.append((p1.get_path(), p2.get_path()))
                            tr.add(p1, p2)
                        else:
                            ui_ = ui.UI()
                            diff_result = diff.DiffParser(p1, p2).parse_diff()
                            ui_.update_text(diff_result, p1.get_path(), p2.get_path())
                            global EQ, NEQ
                            EQ, NEQ = False, False

                            def eq_callback(*_, **__):
                                global EQ, NEQ
                                EQ, NEQ = True, False

                            def neq_callback(*_, **__):
                                global EQ, NEQ
                                EQ, NEQ = False, True

                            ui_.eq_action(eq_callback)
                            ui_.neq_action(neq_callback)
                            ui_.main_loop()

                            if EQ:
                                eq.append((p1.get_path(), p2.get_path()))
                                tr.add(p1, p2)
                            elif NEQ:
                                neq.append((p1.get_path(), p2.get_path()))
                            else:
                                raise RuntimeError('no button pressed')

        return ProblemResult(eq, neq)
