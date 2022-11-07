import subprocess
import tempfile
from functools import cache
from typing import *


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
        subp.wait(timeout=2)
        output = subp.stdout.read()
        return output, subp.returncode

    @cache
    def get_path(self) -> str:
        return self.__path__
