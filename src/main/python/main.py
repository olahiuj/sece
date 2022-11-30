#!/bin/python
import os
import sys
from typing import *

import ui
from problem import Problem, ProblemResult
from closure import Closure
from diff import DiffParser
from program import Program


def handle_path(path: str) -> str:
    if not path.endswith('/'):
        path += '/'
    return path


def argv_sanity_check() -> Tuple[str, str]:
    if len(sys.argv) != 4:
        print("Usage: ./main.py [auto | manual] input_folder output_folder", file=sys.stderr)
        exit(1)
    if sys.argv[1] in ['auto', 'manual']:
        input_folder = handle_path(sys.argv[2])
        output_folder = handle_path(sys.argv[3])
        return input_folder, output_folder
    else:
        print("Usage: ./main.py [auto | manual] input_folder output_folder", file=sys.stderr)
        exit(1)


def main() -> List[ProblemResult]:
    path1, path2 = argv_sanity_check()

    is_manual = True if sys.argv[1] == 'manual' else False
    input_folder, output_folder = path1, path2
    result = []
    for p in os.listdir(input_folder):
        prob = Problem(input_folder + p + "/")
        print(f"==={prob.get_folder()}===")
        result.append(prob.solve(is_manual))

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
