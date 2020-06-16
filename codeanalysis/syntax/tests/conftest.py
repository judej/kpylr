from codeanalysis.syntax.parser import Parser
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax
from codeanalysis.syntax.paranthesizedexpressionsyntax import (
    ParanthesizedExpressionSyntax,
)
from codeanalysis.syntax.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.literalexpressionsyntax import LiteralExpressionSyntax
import pytest


@pytest.fixture
def literal0() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("0", 0, SyntaxKind.numbertoken, 0))


@pytest.fixture
def literal1() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("2", 0, SyntaxKind.numbertoken, 2))


@pytest.fixture
def literal2() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("3", 0, SyntaxKind.numbertoken, 3))


@pytest.fixture
def open_paranthesis() -> SyntaxToken:
    return SyntaxToken("(", 0, SyntaxKind.openparanthesistoken, None)


@pytest.fixture
def close_paranthesis() -> SyntaxToken:
    return SyntaxToken(")", 0, SyntaxKind.closeparanthesistoken, None)


@pytest.fixture
def addition_operator() -> SyntaxToken:
    return SyntaxToken("+", 0, SyntaxKind.additiontoken, None)


@pytest.fixture
def subtraction_operator() -> SyntaxToken:
    return SyntaxToken("-", 0, SyntaxKind.subtractiontoken, None)


@pytest.fixture
def multiplication_operator() -> SyntaxToken:
    return SyntaxToken("*", 0, SyntaxKind.multiplicationtoken, None)


@pytest.fixture
def division_operator() -> SyntaxToken:
    return SyntaxToken("/", 0, SyntaxKind.divisiontoken, None)


@pytest.fixture
def binary_expression_syntax_simple(
    literal1, literal2, addition_operator
) -> BinaryExpressionSyntax:
    return BinaryExpressionSyntax(literal1, addition_operator, literal2)


@pytest.fixture
def paranthesized_expression_simple(
    literal1, literal2, addition_operator, open_paranthesis, close_paranthesis
) -> ParanthesizedExpressionSyntax:
    return ParanthesizedExpressionSyntax(
        open_paranthesis,
        BinaryExpressionSyntax(literal1, addition_operator, literal2),
        close_paranthesis,
    )


@pytest.fixture
def parser_simple(
    literal1, literal2, addition_operator, open_paranthesis, close_paranthesis
) -> Parser:
    return Parser("2+3", 0)
