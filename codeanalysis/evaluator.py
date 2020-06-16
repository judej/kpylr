from codeanalysis.unaryexpressionsyntax import UnaryExpressionSyntax
from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.literalexpressionsyntax import LiteralExpressionSyntax
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax


class Evaluator:
    def __init__(self, root: ExpressionSyntax) -> None:
        self.root = root

    def evaluate(self) -> int:
        return self.evaluate_expression(self.root)

    def evaluate_expression(self, expr: ExpressionSyntax) -> int:
        # we need to deal with Binary expressions and literal expressions now
        if isinstance(expr, LiteralExpressionSyntax):
            return expr.literal_token.value
        elif isinstance(expr, UnaryExpressionSyntax):
            operand = self.evaluate_expression(expr.operand)
            if expr.operator_token.kind() == SyntaxKind.subtractiontoken:
                operand *= -1
            elif expr.operator_token.kind() != SyntaxKind.additiontoken:
                raise Exception(
                    f"Unexpected unary operator: {expr.operator_token.kind()}"
                )  # TODO figure out correct exception
            return operand

        elif isinstance(expr, BinaryExpressionSyntax):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            switcher = {
                SyntaxKind.additiontoken: left + right,
                SyntaxKind.subtractiontoken: left - right,
                SyntaxKind.multiplicationtoken: left * right,
                SyntaxKind.divisiontoken: left / right,  # TODO: handle div by 0
            }
            return switcher.get(expr.operator_token.kind(), 0)
        elif isinstance(expr, ParanthesizedExpressionSyntax):
            return self.evaluate_expression(expr.expression)


class BadBinaryExpressionOperatorException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """

    pass


class UnexpectedBinaryExpressionNodeException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """

    pass
