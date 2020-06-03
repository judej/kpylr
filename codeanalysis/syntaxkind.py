from enum import Enum


class SyntaxKind(Enum):
    """Kinds of Syntax Tokens
    """

    number = (1,)
    string = (2,)
    addition = (3,)
    subtraction = (4,)
    multiplication = (5,)
    division = (6,)
    whitespace = (7,)
    openparanthesis = (8,)
    closeparanthesis = (9,)
    badtoken = (10,)
    binaryexpression = (11,)
    paranthesizedexpression = (12,)
    endoffile = 13
