"""This module provides Problem abstraction for each subfolder under input/"""
import dataclasses
import os
from typing import List, Tuple

import diff
import ui
from checker import Checker
from generator import Input, Char, Int, String, GeneratorRAND
from program import Program
from closure import Closure

EQ, NEQ = False, False


@dataclasses.dataclass
class ProblemResult:
    """a list of equal and inequal pairs of program names"""
    equal_pairs: List[Tuple[str, str]]
    inequal_pairs: List[Tuple[str, str]]


class ParserException(BaseException):
    """ParserException is thrown when it fails to parse stdin_format.txt"""
    def __init__(self, message: str):
        super(self).__init__(message)


def parse(stdin_format: str) -> Input:
    """stdin_format.txt parser

    This is the parser that parses stdin_format.txt and returns
    a list of lines. Each line contains a list of Data.
    """
    result = []
    for line in stdin_format.strip().split('\n'):
        line_result = []
        for token in line.strip().split():
            if token[0] == 'i':
                (lower, upper) = token.split(',')
                line_result.append(
                    Int(
                        int(lower.removeprefix('int(')),
                        int(upper.removesuffix(')'))
                    )
                )
            elif token[0] == 's':
                (lower, upper) = token.split(',')
                line_result.append(
                    String(
                        int(lower.removeprefix('string(')),
                        int(upper.removesuffix(')'))
                    )
                )
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
        for filename in os.listdir(folder):
            abs_file_path = folder + filename
            if filename.endswith(".c") or filename.endswith(".cpp"):
                self.__programs__.append(Program(abs_file_path))
            elif filename == "stdin_format.txt":
                with open(abs_file_path, encoding="utf-8") as file:
                    self.__stdin_format__ = file.readlines()

        if not self.__stdin_format__:
            raise RuntimeError("stdin_format.txt not found")

    def programs(self) -> List[Program]:
        """programs getter"""
        return self.__programs__

    def get_input_format(self) -> Input:
        """input format getter"""
        return parse(''.join(self.__stdin_format__))

    def get_folder(self) -> str:
        """folder path getter"""
        return self.__folder__

    def solve(self, is_manual: bool) -> ProblemResult:
        """check equivalences of all programs in this Problem"""
        neq_result, eq_result = [], []
        transitive_closure = Closure(set())
        programs: List[Program] = self.programs()
        for (index1, program1) in enumerate(programs):
            for index2 in range(index1):
                program2 = programs[index2]
                if not transitive_closure.contains(program1, program2):
                    gen = GeneratorRAND(self.get_input_format())
                    if not Checker().check(program1, program2, gen):
                        neq_result.append((program1.get_path(), program2.get_path()))
                    else:
                        if not is_manual:
                            eq_result.append((program1.get_path(), program2.get_path()))
                            transitive_closure.add(program1, program2)
                        else:
                            ui_ = ui.UI()
                            diff_result = diff.DiffParser(program1, program2).parse_diff()
                            ui_.update_text(diff_result, program1.get_path(), program2.get_path())
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
                                eq_result.append((program1.get_path(), program2.get_path()))
                                transitive_closure.add(program1, program2)
                            elif NEQ:
                                neq_result.append((program1.get_path(), program2.get_path()))
                            else:
                                raise RuntimeError('no button pressed')

        return ProblemResult(eq_result, neq_result)
