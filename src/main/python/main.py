#!/bin/python
import os
import sys
from typing import *

from problem import Problem, ProblemResult


def handle_path(path: str) -> str:
    if not path.endswith('/'):
        path += '/'
    return path


def argv_sanity_check() -> Tuple[str, str]:
    if len(sys.argv) != 3:
        print("Usage: ./main.py input_folder output_folder", file=sys.stderr)
        exit(1)
    input_folder = handle_path(sys.argv[1])
    output_folder = handle_path(sys.argv[2])
    return input_folder, output_folder


def main() -> List[ProblemResult]:
    input_folder, output_folder = argv_sanity_check()

    result = []
    for p in os.listdir(input_folder):
        prob = Problem(input_folder + p + "/")
        print(f"==={prob.get_folder()}===")
        result.append(prob.solve())

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    with open(f"{output_folder}equal.csv", "w") as eq:
        eq.writelines(["file1, file2\n"])
        for each in result:
            for p in each.equal_pairs:
                eq.writelines([f"{p[0]}, {p[1]}\n"])

    with open(f"{output_folder}inequal.csv", "w") as eq:
        eq.writelines(["file1, file2\n"])
        for each in result:
            for p in each.inequal_pairs:
                eq.writelines([f"{p[0]}, {p[1]}\n"])

    return result


if __name__ == "__main__":
    main()
