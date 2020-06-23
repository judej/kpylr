from codeanalysis.syntax.syntaxkind import SyntaxKind
import pytest
from codeanalysis.syntax.literalexpressionsyntax import LiteralExpressionSyntax


class TestLiteralExpressionSyntax:
    def test_kind(self, literal0: LiteralExpressionSyntax, literal1: LiteralExpressionSyntax) -> None:
        assert literal0.kind() == SyntaxKind.numbertoken

    def test_getChildren(self, literal0: LiteralExpressionSyntax) -> None:
        literal = literal0.get_children()
        assert next(literal).kind() == SyntaxKind.numbertoken
        with pytest.raises(Exception) as excinfo:
            next(literal)
        assert str(excinfo) == "<ExceptionInfo StopIteration() tblen=1>"

    def test_getLastChild(self, literal0: LiteralExpressionSyntax) -> None:
        assert literal0.get_last_child().kind() == SyntaxKind.numbertoken
