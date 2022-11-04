from typing import *
from generator import Input


class Parser():
    """stdin_format.txt parser

    This is the parser that parses stdin_format.txt and returns
    a list of lines. Each line contains a list of Data.
    """

    @classmethod
    def parse(input: str) -> Input:
        pass


class Program():
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


class Problem():
    """a subfolder of the input folder

    This class represents exactly one subfolder under the input
    folder. Equivalence of all programs in one Problem should 
    be checked.
    """

    def __init__(self, folder: str) -> None:
        pass

    def programs() -> List[Program]:
        pass

    def get_input_format() -> Input:
        pass
