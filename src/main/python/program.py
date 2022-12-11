"""This module provides source code abstraction."""
import os
import subprocess
import tempfile
from dataclasses import dataclass
from typing import IO, Tuple


@dataclass
class SUCCESS:
    """Program exited normally"""


@dataclass
class TIMEOUT:
    """Program timeout"""


@dataclass
class CRASHED:
    """Program crashed"""
    exit_code: int


ProgramResult = SUCCESS | TIMEOUT | CRASHED


class Program:
    """one program source code

    This is the internal representation of source program found
    in each subfolder of the input folder.
    """

    def __init__(self, path: str) -> None:
        self.__executable__ = None
        self.__path__ = path

    def compile(self) -> None:
        """compile this program to get executable"""
        # system(f"{compiler} {path} -O3 -o {executable.name} &> /dev/null")
        path = self.__path__
        with tempfile.NamedTemporaryFile("w+") as executable:
            executable.write("hh")
            executable.close()
            self.__executable__ = executable

            if path.endswith(".cpp"):
                compiler = "g++"
            elif path.endswith(".c"):
                compiler = "gcc"
            else:
                raise RuntimeError()

            with subprocess.Popen(
                [compiler, path, "-O3", "-o", executable.name],
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            ) as pcomp:
                pcomp.wait(timeout=10)
                if pcomp.returncode != 0:
                    raise RuntimeError()

    def get_executable(self) -> IO:
        """compiled executable file getter"""
        if self.__executable__ is None or not os.path.exists(self.__executable__.name):
            self.compile()
        return self.__executable__

    def run(self, input_file: IO) -> Tuple[bytes, ProgramResult]:
        """run this program and generate (stdout, result)

        Args:
            input_file (IO): path to generated input file

        Returns:
            Tuple[str, ProgramResult]: (stdout, SUCCESS | TIMEOUT | CRASHED(exit_code))
        """
        with subprocess.Popen(
            [self.get_executable().name],
            stdin=input_file,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        ) as subp:
            try:
                subp.wait(timeout=2)
                output = subp.stdout.read()
            except subprocess.TimeoutExpired:
                return bytes(), TIMEOUT()

            if subp.returncode == 0:
                return output, SUCCESS()

            return output, CRASHED(subp.returncode)

    def get_path(self) -> str:
        """source code path getter"""
        return self.__path__
