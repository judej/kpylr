from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.numberexpressionsyntax import NumberExpressionSyntax
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax
from codeanalysis.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax

class Evaluator:
    def __init__(self, root: ExpressionSyntax) -> None:
        self.root = root

    def evaluate(self) -> int:
        return self.evaluate_expression(self.root)

    def evaluate_expression(self, expr: ExpressionSyntax) -> int:
        # we need to deal with Binary expressions and number expressions now
        if isinstance(expr, NumberExpressionSyntax):
            return expr.numberToken.value
        elif isinstance(expr, BinaryExpressionSyntax):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            switcher = {
                SyntaxKind.addition: left + right,
                SyntaxKind.subtraction: left - right,
                SyntaxKind.multiplication: left * right,
                SyntaxKind.division: left / right,
            }
            return switcher.get(expr.operatorToken.kind(), 0)
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
