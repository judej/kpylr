from codeanalysis.parser import Parser
from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.numberexpressionsyntax import NumberExpressionSyntax
import pytest


@pytest.fixture
def number0() -> NumberExpressionSyntax:
    return NumberExpressionSyntax(SyntaxToken("0", 0, SyntaxKind.number, 0))


@pytest.fixture
def number1() -> NumberExpressionSyntax:
    return NumberExpressionSyntax(SyntaxToken("2", 0, SyntaxKind.number, 2))


@pytest.fixture
def number2() -> NumberExpressionSyntax:
    return NumberExpressionSyntax(SyntaxToken("3", 0, SyntaxKind.number, 3))


@pytest.fixture
def open_paranthesis() -> SyntaxToken:
    return SyntaxToken("(", 0, SyntaxKind.openparanthesis, None)


@pytest.fixture
def close_paranthesis() -> SyntaxToken:
    return SyntaxToken(")", 0, SyntaxKind.closeparanthesis, None)


@pytest.fixture
def addition_operator() -> SyntaxToken:
    return SyntaxToken("+", 0, SyntaxKind.addition, None)


@pytest.fixture
def subtraction_operator() -> SyntaxToken:
    return SyntaxToken("-", 0, SyntaxKind.subtraction, None)


@pytest.fixture
def multiplication_operator() -> SyntaxToken:
    return SyntaxToken("*", 0, SyntaxKind.multiplication, None)


@pytest.fixture
def division_operator() -> SyntaxToken:
    return SyntaxToken("/", 0, SyntaxKind.division, None)


@pytest.fixture
def binary_expression_syntax_simple(
    number1, number2, addition_operator
) -> BinaryExpressionSyntax:
    return BinaryExpressionSyntax(number1, addition_operator, number2)


@pytest.fixture
def paranthesized_expression_simple(
    number1, number2, addition_operator, open_paranthesis, close_paranthesis
) -> ParanthesizedExpressionSyntax:
    return ParanthesizedExpressionSyntax(
        open_paranthesis,
        BinaryExpressionSyntax(number1, addition_operator, number2),
        close_paranthesis,
    )


@pytest.fixture
def parser_simple(
    number1, number2, addition_operator, open_paranthesis, close_paranthesis
) -> Parser:
    return Parser("2+3", 0)
