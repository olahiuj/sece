#!/bin/python
import os
import sys
from typing import *

from problem import Problem, ProbResult


def main(input_folder: str) -> List[ProbResult]:
    result = []
    for p in os.listdir(input_folder):
        prob = Problem(input_folder + p + "/")
        print(f"==={prob.get_folder()}===")
        result.append(prob.solve())
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main.py input_folder", file=sys.stderr)
        exit(1)
    main(sys.argv[1])
