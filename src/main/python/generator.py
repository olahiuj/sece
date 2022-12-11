"""
This module provides a random Generator to generate inputs.
"""
import random
import string
from dataclasses import dataclass
from typing import List, Iterable


@dataclass
class Char:
    """input type of Char"""


@dataclass
class Int:
    """input type of Int with value in [mn_val, mx_val]"""
    mn_val: int
    mx_val: int


@dataclass
class String:
    """input type of String with length in [mn_len, mx_len]"""
    mn_len: int
    mx_len: int


Data = Char | Int | String

InputLine = List[Data]

Input = List[InputLine]


def gen_random(data: Data) -> str:
    """generate random input for given input type"""
    match data:
        case Char():
            return random.choice(string.ascii_letters)
        case Int(mn_val, mx_val):
            return str(random.randint(mn_val, mx_val))
        case String(mn_len, mx_len):
            length = random.randint(mn_len, mx_len)
            return "".join([gen_random(Char()) for _ in range(length)])


class Generator:
    """input generator

    Inherit this class and override method gen() to create
    more input generators.
    """

    def __init__(self, stdin: Input) -> None:
        self.__stdin__ = stdin

    def gen(self) -> Iterable[str]:
        """generate lines of inputs"""


class GeneratorRAND(Generator):
    """random input generator"""
    def gen(self) -> Iterable[str]:
        """generate random inputs"""
        for line in self.__stdin__:
            yield " ".join(map(gen_random, line))
