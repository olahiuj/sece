from typing import *
from dataclasses import dataclass


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
            pass
        case Int(mn, mx):
            pass
        case String(mn_len, mx_len):
            pass


def gen_all(data: Data) -> List[str]:
    match data:
        case Char():
            pass
        case Int(mn, mx):
            pass
        case String(mn_len, mx_len):
            pass


class Genrator():
    """input generator

    Inherit this class and override method gen() to create
    more input generators.
    """

    def __init__(self, input: Input) -> None:
        self.__input__ = input

    def gen(self) -> List[str]:
        pass


class Generator_ONCE(Generator):
    def __init__(self, input: Input) -> None:
        super().__init__(input)

    def gen(self) -> List[str]:
        pass


class Generator_ALL(Generator):
    def __init__(self, input: Input) -> None:
        super().__init__(input)

    def gen(self) -> List[str]:
        pass
