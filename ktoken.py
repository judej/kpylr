from enum import Enum
from typing import Any

class SyntaxKind(Enum):
    number = 1,
    string = 2,
    addition = 3,
    subtraction = 4, 
    multiplication = 5,
    division = 6,
    whitespace = 7,
    openparanthesis = 8,
    closeparanthesis = 9,
    endoffile = 10,
    badtoken = 11

class SyntaxToken:
    def __init__(cls, text: str, position: int, kind: SyntaxKind, value: Any) -> None:
        cls.text = text
        cls.postion = position
        cls.kind = kind
        cls.value = value
        





