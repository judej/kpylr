from codeanalysis.binding.boundbinaryoperatorkind import BoundBinaryOperatorKind
from codeanalysis.binding.boundexpression import BoundExpression


class BoundBinaryExpression(BoundExpression):
    def __init__(self, left: BoundExpression, operator_kind: BoundBinaryOperatorKind, right: BoundExpression) -> None:
        self.operator_kind = operator_kind
        self.left = left
        self.right = right

