from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.tests.conftest import paranthesized_expression_simple
import pytest


class TestParanthesizedExpressionSyntax:
    def test_kind(self, paranthesized_expression_simple) -> None:
        assert (
            paranthesized_expression_simple.kind() == SyntaxKind.paranthesizedexpression
        )

    def test_getChildren(self, paranthesized_expression_simple) -> None:
        token_gernator = paranthesized_expression_simple.get_children()
        assert next(token_gernator).kind() == SyntaxKind.openparanthesistoken
        assert next(token_gernator).kind() == SyntaxKind.binaryexpression
        assert next(token_gernator).kind() == SyntaxKind.closeparanthesistoken
        with pytest.raises(Exception) as excinfo:
            next(token_gernator)
        assert str(excinfo) == "<ExceptionInfo StopIteration() tblen=1>"

    def test_getLastChild(self, paranthesized_expression_simple) -> None:
        assert (
            paranthesized_expression_simple.get_last_child().kind()
            == SyntaxKind.closeparanthesistoken
        )

