#!/bin/python
"""This is the main module for sece."""
import os
import sys
from typing import Tuple, List
from problem import Problem, ProblemResult


def handle_path(path: str) -> str:
    """simple folder path treatment. too lazy to use pathlib ;-P"""
    if not path.endswith('/'):
        path += '/'
    return path


def argv_sanity_check() -> Tuple[str, str] | None:
    """sanity check for sys.argv, exit(1) if malicious"""
    if len(sys.argv) == 4 and sys.argv[1] in ['auto', 'manual']:
        input_folder = handle_path(sys.argv[2])
        output_folder = handle_path(sys.argv[3])
        return input_folder, output_folder
    print(
        "Usage: ./main.py [auto | manual] input_folder output_folder",
        file=sys.stderr
    )
    sys.exit(1)


def main() -> List[ProblemResult]:
    """main procedure for sece"""
    path1, path2 = argv_sanity_check()

    is_manual = sys.argv[1] == 'manual'
    input_folder, output_folder = path1, path2
    result = []
    for prob_name in os.listdir(input_folder):
        prob = Problem(input_folder + prob_name + "/")
        print(f"==={prob.get_folder()}===")
        result.append(prob.solve(is_manual))

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    with open(f"{output_folder}equal.csv", "w", encoding="utf-8") as equal_file:
        equal_file.writelines(["file1, file2\n"])
        for each in result:
            for (elem1, elem2) in each.equal_pairs:
                equal_file.writelines([f"{elem1}, {elem2}\n"])

    with open(f"{output_folder}inequal.csv", "w", encoding="utf-8") as inequal_file:
        inequal_file.writelines(["file1, file2\n"])
        for each in result:
            for (elem1, elem2) in each.inequal_pairs:
                inequal_file.writelines([f"{elem1}, {elem2}\n"])

    return result


if __name__ == "__main__":
    main()
