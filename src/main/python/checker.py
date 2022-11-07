import tempfile

from generator import Generator
from program import Program


class Checker:
    """equivalence checker"""

    @staticmethod
    def check(p1: Program, p2: Program, generator: Generator) -> bool:
        """equivalence checker

        Args:
            p1 (Program): the first program
            p2 (Program): the second program
            generator (Generator): given input generator

        Returns:
            bool: if they're equivalent
        """
        data_in = generator.gen()
        input_file = tempfile.TemporaryFile("w+")
        input_file.writelines(data_in)
        result1 = p1.run(input_file)
        result2 = p2.run(input_file)
        return result1 == result2
