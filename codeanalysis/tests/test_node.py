import pytest
from ..node import ExpressionSyntax, SyntaxKind, SyntaxNode, SyntaxToken


class TestSyntaxNode:
    with pytest.raises(Exception) as excinfo:
        testsn = SyntaxNode()
    assert (
        str(excinfo.value)
        == "Can't instantiate abstract class SyntaxNode with abstract methods getChildren, kind"
    )


class TestExpressionSyntax:
    with pytest.raises(Exception) as excinfo:
        expressionSyntax = ExpressionSyntax()
    assert (
        str(excinfo.value)
        == "Can't instantiate abstract class ExpressionSyntax with abstract methods getChildren, getLastChild, kind"
    )


class TestSyntaxToken:
    def test_create_syntax_token(self):
        syntaxToken = SyntaxToken("2+3", 1, SyntaxKind.addition, None)
        assert True

    def test_getChildren(self):
        syntaxToken = SyntaxToken("2+3", 1, SyntaxKind.addition, None)
        assert True

    def test_getLastChild(self):
        assert True

    def test_kind(self):
        assert True


class TestNumberExpressionSyntax:
    def test_kind(self):
        assert True

    def test_getChildren(self):
        assert True

    def test_getLastChild(self):
        assert True


class TestBinaryExpressionSyntax:
    def test_kind(self):
        assert True

    def test_getChildren(self):
        assert True

    def test_getLastChild(self):
        assert True

