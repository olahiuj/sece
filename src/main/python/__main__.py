#!/bin/python

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./__main__.py input_folder", file=sys.stderr)
        exit(1)
