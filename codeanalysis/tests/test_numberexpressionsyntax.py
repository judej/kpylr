from codeanalysis.syntaxkind import SyntaxKind
import pytest
from codeanalysis.numberexpressionsyntax import NumberExpressionSyntax


class TestNumberExpressionSyntax:
    def test_kind(
        self, number0: NumberExpressionSyntax, number1: NumberExpressionSyntax
    ) -> None:
        assert number0.kind() == SyntaxKind.number

    def test_getChildren(self, number0: NumberExpressionSyntax) -> None:
        number = number0.get_children()
        assert next(number).kind() == SyntaxKind.number
        with pytest.raises(Exception) as excinfo:
            next(number)
        assert str(excinfo) == "<ExceptionInfo StopIteration() tblen=1>"

    def test_getLastChild(self, number0: NumberExpressionSyntax) -> None:
        assert number0.get_last_child().kind() == SyntaxKind.number
