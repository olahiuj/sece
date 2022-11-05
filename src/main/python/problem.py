import os
import subprocess
from functools import cache
from os import system
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
        self.__path__ = path

    def run(self, input_file: IO) -> Tuple[bytes, int]:
        """run this program and generate (stdout, exit code)

        Args:
            input_file (IO): path to generated input file

        Returns:
            Tuple[str, int]: stdout and exit code
        """
        path = self.__path__
        if path.endswith(".cpp"):
            system(f"g++ {path} -O3 -o ./tmp.out")
        elif path.endswith(".c"):
            system(f"gcc {path} -O3 -o ./tmp.out")
        else:
            raise RuntimeError()
        subp = subprocess.Popen(["./tmp.out"], stdout=subprocess.PIPE, stdin=input_file)
        subp.wait(timeout=2)
        output = subp.stdout.read()
        return output, subp.returncode


class Problem:
    """a subfolder of the input folder

    This class represents exactly one subfolder under the input
    folder. Equivalence of all programs in one Problem should 
    be checked.
    """

    def __init__(self, folder: str) -> None:
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
