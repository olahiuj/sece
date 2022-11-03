from typing import *
from problem import Program
from generator import Generator


class Checker():
    """equivalence checker"""

    @classmethod
    def check(p1: Program, p2: Program, generator: Generator) -> bool:
        """equivalence checker

        Args:
            p1 (Program): the first program
            p2 (Program): the second program
            generator (Generator): given input generator

        Returns:
            bool: if they're equivalent
        """
        pass
