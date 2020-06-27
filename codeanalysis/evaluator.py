from typing import Union
from codeanalysis.syntax.unaryexpressionsyntax import UnaryExpressionSyntax
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.literalexpressionsyntax import LiteralExpressionSyntax
from codeanalysis.syntax.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.syntax.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax


class Evaluator:
    def __init__(self, root: ExpressionSyntax) -> None:
        self.root = root

    def evaluate(self) -> Union[int, float]:
        return self.evaluate_expression(self.root)

    def evaluate_expression(self, expr: ExpressionSyntax) -> Union[int, float]:
        # we need to deal with Binary expressions and literal expressions now
        if isinstance(expr, LiteralExpressionSyntax):
            return expr.literal_token.value
        elif isinstance(expr, UnaryExpressionSyntax):
            operand = self.evaluate_expression(expr.operand)
            if expr.operator_token.kind == SyntaxKind.subtractiontoken:
                operand *= -1
            elif expr.operator_token.kind != SyntaxKind.additiontoken:
                raise Exception(
                    f"Unexpected unary operator: {expr.operator_token.kind}"
                )  # TODO figure out correct exception
            return operand

        elif isinstance(expr, BinaryExpressionSyntax):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            if expr.operator_token.kind == SyntaxKind.additiontoken:
                return left + right
            elif expr.operator_token.kind == SyntaxKind.subtractiontoken:
                return left - right
            elif expr.operator_token.kind == SyntaxKind.multiplicationtoken:
                return left * right
            elif expr.operator_token.kind == SyntaxKind.divisiontoken:
                if right == 0:
                    raise ZeroDivisionError
                return left / right

        elif isinstance(expr, ParanthesizedExpressionSyntax):
            return self.evaluate_expression(expr.expression)

        raise Exception("Unknown Expression")


class BadBinaryExpressionOperatorException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """

    pass


class UnexpectedBinaryExpressionNodeException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """

    pass
