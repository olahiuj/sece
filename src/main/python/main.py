#!/bin/python
import os
import sys

import checker
from generator import GeneratorRAND
from problem import Problem


def main(input_folder: str) -> None:
    for p in os.listdir(input_folder):
        prob = Problem(input_folder + p + "/")
        programs = prob.programs()
        for p1 in range(len(programs)):
            for p2 in range(p1):
                stdin = prob.get_input_format()
                g = GeneratorRAND(stdin)
                print(p1, p2, checker.Checker.check(programs[p1], programs[p2], g))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main.py input_folder", file=sys.stderr)
        exit(1)
    main(sys.argv[1])
