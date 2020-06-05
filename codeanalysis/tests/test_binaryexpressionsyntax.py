from codeanalysis.tests.conftest import binary_expression_syntax_simple
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.literalexpressionsyntax import LiteralExpressionSyntax
import pytest
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax


class TestBinaryExpressionSyntax:
    def test_kind(
        self, binary_expression_syntax_simple: BinaryExpressionSyntax
    ) -> None:
        assert binary_expression_syntax_simple.kind() == SyntaxKind.binaryexpression

    def test_getChildren(
        self, binary_expression_syntax_simple: BinaryExpressionSyntax
    ) -> None:
        token_gernator = binary_expression_syntax_simple.get_children()
        assert next(token_gernator).kind() == SyntaxKind.literal
        assert next(token_gernator).kind() == SyntaxKind.addition
        assert next(token_gernator).kind() == SyntaxKind.literal
        with pytest.raises(Exception) as excinfo:
            next(token_gernator)
        assert str(excinfo) == "<ExceptionInfo StopIteration() tblen=1>"

    def test_getLastChild(
        self, binary_expression_syntax_simple: BinaryExpressionSyntax
    ) -> None:
        assert (
            binary_expression_syntax_simple.get_last_child().kind()
            == SyntaxKind.literal
        )
