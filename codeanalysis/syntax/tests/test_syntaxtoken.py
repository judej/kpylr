from codeanalysis.syntax.tests.conftest import (
    addition_operator,
    division_operator,
    multiplication_operator,
    subtraction_operator,
)
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxkind import SyntaxKind


class TestSyntaxToken:
    def test_create_syntax_token(
        self,
        addition_operator: SyntaxToken,
        subtraction_operator: SyntaxToken,
        division_operator: SyntaxToken,
        multiplication_operator: SyntaxToken,
    ):
        assert addition_operator.kind() == SyntaxKind.additiontoken
        assert subtraction_operator.kind() == SyntaxKind.subtractiontoken
        assert division_operator.kind() == SyntaxKind.divisiontoken
        assert multiplication_operator.kind() == SyntaxKind.multiplicationtoken

    def test_get_children(self, addition_operator: SyntaxToken):
        assert next(addition_operator.get_children()) == None

    def test_get_last_child(self, addition_operator: SyntaxToken):
        assert addition_operator.get_last_child() == None

    def test_kind(self, addition_operator: SyntaxToken):
        assert addition_operator.kind() == SyntaxKind.additiontoken

