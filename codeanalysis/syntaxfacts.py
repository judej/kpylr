from codeanalysis.syntaxkind import SyntaxKind


class SyntaxFacts:
    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int:
        # returning 1 if it is a binary operator
        if kind in {SyntaxKind.additiontoken, SyntaxKind.subtractiontoken}:
            return 1
        elif kind in {
            SyntaxKind.multiplicationtoken,
            SyntaxKind.divisiontoken,
        }:
            return 2
        return 0
