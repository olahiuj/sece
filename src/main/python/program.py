import subprocess
import tempfile
from dataclasses import dataclass
from functools import cache
from typing import *


@dataclass
class SUCCESS:
    pass


@dataclass
class TIMEOUT:
    pass


@dataclass
class CRASHED:
    exit_code: int


ProgramResult = SUCCESS | TIMEOUT | CRASHED


class Program:
    """one program source code

    This is the internal representation of source program found
    in each subfolder of the input folder.
    """

    def __init__(self, path: str) -> None:
        self.__path__ = path

    def run(self, input_file: IO) -> Tuple[bytes, ProgramResult]:
        """run this program and generate (stdout, result)

        Args:
            input_file (IO): path to generated input file

        Returns:
            Tuple[str, ProgramResult]: (stdout, SUCCESS | TIMEOUT | CRASHED(exit_code))
        """
        path = self.__path__
        executable = tempfile.NamedTemporaryFile("w+")
        executable.write("hh")
        executable.close()

        if path.endswith(".cpp"):
            compiler = "g++"
        elif path.endswith(".c"):
            compiler = "gcc"
        else:
            raise RuntimeError()

        pcomp = subprocess.Popen(
            [compiler, path, "-O3", "-o", executable.name],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        pcomp.wait(timeout=10)
        if pcomp.returncode != 0:
            raise RuntimeError()
        # system(f"{compiler} {path} -O3 -o {executable.name} &> /dev/null")
        subp = subprocess.Popen([executable.name], stdout=subprocess.PIPE, stdin=input_file)
        try:
            subp.wait(timeout=2)
            output = subp.stdout.read()
        except subprocess.TimeoutExpired as e:
            return bytes(), TIMEOUT()

        if subp.returncode == 0:
            return output, SUCCESS()
        else:
            return output, CRASHED(subp.returncode)

    @cache
    def get_path(self) -> str:
        return self.__path__
