from enum import Enum


class SyntaxKind(Enum):
    """Kinds of Syntax Tokens
    """

    # tokens
    badtoken = (0,)
    endoffile = (1,)
    number = (2,)
    string = (3,)
    whitespace = (4,)

    # operators
    addition = (5,)
    subtraction = (6,)
    multiplication = (7,)
    division = (8,)
    openparanthesis = (9,)
    closeparanthesis = (10,)

    # expressions
    binaryexpression = (11,)
    paranthesizedexpression = (12,)
