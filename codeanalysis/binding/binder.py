from codeanalysis.binding.boundbinaryoperatorkind import BoundBinaryOperatorKind
from codeanalysis.binding.boundbinaryexpression import BoundBinaryExpression
from codeanalysis.binding.boundexpression import BoundExpression
from codeanalysis.syntax.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax


class binder:
    def __init__(self) -> None:
        pass

    def bind_expression(self, syntax: ExpressionSyntax) -> BoundExpression:
        if syntax.kind == SyntaxKind.binaryexpression:
            return self._bind_binary_expression(syntax)
        else:
            raise Exception("unknown sybtax kind")

    def _bind_binary_expression(self, syntax: BinaryExpressionSyntax) -> BoundBinaryExpression:
        bound_left = self.bind_expression(syntax.left)
        bound_operator_binary_kind = self._bound_binary_operator_kind(syntax.operator_token.kind)
        bound_right = self.bind_expression(syntax.right)
        return BoundBinaryExpression(bound_left, bound_operator_binary_kind, bound_right)

    def _bound_binary_operator_kind(self, kind: SyntaxKind) -> BoundBinaryOperatorKind:
        if kind == SyntaxKind.additiontoken:
            return BoundBinaryOperatorKind.addition
        elif kind == SyntaxKind.subtractiontoken:
            return BoundBinaryOperatorKind.subtraction
        elif kind == SyntaxKind.multiplicationtoken:
            return BoundBinaryOperatorKind.multiplication
        elif kind == SyntaxKind.divisiontoken:
            return BoundBinaryOperatorKind.division
        raise Exception("unexpected unary operator")

