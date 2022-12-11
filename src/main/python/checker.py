"""
This module provides equivalence checker.
Only one simple Testing based Checker class is provided.
"""
import tempfile

from generator import Generator
from program import Program


class Checker:
    """testing based equivalence checker"""
    def __init__(self, run_times=4):
        self.__run_times__: int = run_times

    def check(self, program1: Program, program2: Program, generator: Generator) -> bool:
        """equivalence checker

        Args:
            program1 (Program): the first program
            program2 (Program): the second program
            generator (Generator): given input generator

        Returns:
            bool: if they're equivalent
        """
        for _ in range(self.__run_times__):
            data_in = generator.gen()
            input_file = tempfile.TemporaryFile("w+")
            input_file.writelines(data_in)
            result1 = program1.run(input_file)
            result2 = program2.run(input_file)
            if result1 != result2:
                return False
        return True

    def set_run_times(self, run_times):
        """update number of rounds to run on random input"""
        self.__run_times__ = run_times
