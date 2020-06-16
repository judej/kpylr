from enum import Enum


class SyntaxKind(Enum):
    """Kinds of Syntax Tokens
    """

    # tokens
    badtoken = (0,)
    endoffiletoken = (1,)
    whitespacetoken = (2,)
    numbertoken = (3,)

    # operators
    additiontoken = (5,)
    subtractiontoken = (6,)
    multiplicationtoken = (7,)
    divisiontoken = (8,)
    openparanthesistoken = (9,)
    closeparanthesistoken = (10,)

    # expressions
    literalexpression = (11,)
    binaryexpression = (12,)
    paranthesizedexpression = (13,)
    unaryexpression = (14,)
