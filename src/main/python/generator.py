import random
import string
from dataclasses import dataclass
from functools import reduce
from typing import *


@dataclass
class Char:
    pass


@dataclass
class Int:
    mn: int
    mx: int


@dataclass
class String:
    mn_len: int
    mx_len: int


Data = Char | Int | String

InputLine = List[Data]

Input = List[InputLine]


def gen_random(data: Data) -> str:
    match data:
        case Char():
            return random.choice(string.ascii_letters)
        case Int(mn, mx):
            return str(random.randint(mn, mx))
        case String(mn_len, mx_len):
            length = random.randint(mn_len, mx_len)
            return reduce(str.__add__, [gen_random(Char()) for x in range(length)])


def gen_all(data: Data) -> List[str]:
    match data:
        case Char():
            pass
        case Int(mn, mx):
            pass
        case String(mn_len, mx_len):
            pass


class Generator:
    """input generator

    Inherit this class and override method gen() to create
    more input generators.
    """

    def __init__(self, stdin: Input) -> None:
        self.__stdin__ = stdin

    def gen(self) -> List[str]:
        pass


class GeneratorRAND(Generator):
    def __init__(self, stdin: Input) -> None:
        super().__init__(stdin)

    def gen(self) -> Iterable[str]:
        for line in self.__stdin__:
            for data in line:
                yield gen_random(data)


class GeneratorALL(Generator):
    def __init__(self, stdin: Input) -> None:
        super().__init__(stdin)

    def gen(self) -> List[str]:
        pass
