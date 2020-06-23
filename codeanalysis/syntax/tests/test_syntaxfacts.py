from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.syntaxfacts import SyntaxFacts


class TestSyntaxFacts:
    def test_get_unary_operator_precedence(self) -> None:
        assert SyntaxFacts.get_unary_operator_precedence(SyntaxKind.additiontoken) == 3
        assert SyntaxFacts.get_unary_operator_precedence(SyntaxKind.subtractiontoken) == 3
        assert SyntaxFacts.get_unary_operator_precedence(SyntaxKind.multiplicationtoken) == 0
        assert SyntaxFacts.get_unary_operator_precedence(SyntaxKind.divisiontoken) == 0

    def test_get_binary_operator_precedence(self) -> None:
        assert SyntaxFacts.get_binary_operator_precedence(SyntaxKind.additiontoken) == 1
        assert SyntaxFacts.get_binary_operator_precedence(SyntaxKind.subtractiontoken) == 1
        assert SyntaxFacts.get_binary_operator_precedence(SyntaxKind.multiplicationtoken) == 2
        assert SyntaxFacts.get_binary_operator_precedence(SyntaxKind.divisiontoken) == 2
