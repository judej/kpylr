import pytest
from codeanalysis.syntax.syntaxnode import SyntaxNode


class TestSyntaxNode:
    def test_creation(self):
        with pytest.raises(Exception) as excinfo:
            testsn = SyntaxNode()
        assert (
            str(excinfo.value)
            == "Can't instantiate abstract class SyntaxNode with abstract methods get_children, kind"
        )
