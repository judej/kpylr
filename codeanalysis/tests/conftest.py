from codeanalysis.parser import Parser
from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.literalexpressionsyntax import LiteralExpressionSyntax
import pytest


@pytest.fixture
def literal0() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("0", 0, SyntaxKind.literal, 0))


@pytest.fixture
def literal1() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("2", 0, SyntaxKind.literal, 2))


@pytest.fixture
def literal2() -> LiteralExpressionSyntax:
    return LiteralExpressionSyntax(SyntaxToken("3", 0, SyntaxKind.literal, 3))


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
