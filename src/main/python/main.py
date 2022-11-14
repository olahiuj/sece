#!/bin/python
import os
import sys
from typing import *

from problem import Problem, ProblemResult


def input_sanity_check() -> str:
    if len(sys.argv) != 2:
        print("Usage: ./main.py input_folder", file=sys.stderr)
        exit(1)
    path = sys.argv[1]
    if not path.endswith("/"):
        path += "/"
    return path


def main() -> List[ProblemResult]:
    input_folder = input_sanity_check()

    result = []
    for p in os.listdir(input_folder):
        prob = Problem(input_folder + p + "/")
        print(f"==={prob.get_folder()}===")
        result.append(prob.solve())
    return result


if __name__ == "__main__":
    main()
