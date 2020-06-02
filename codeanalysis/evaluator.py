from codeanalysis.node import BinaryExpressionSyntax, ExpressionSyntax, NumberExpressionSyntax, ParanthesizedExpressionSyntax, SyntaxKind
class Evaluator:
    def __init__(self, root: ExpressionSyntax) -> None:
        self.root = root
    
    def Evaluate(self) -> int:
        return self.EvaluateExpression(self.root)

    def EvaluateExpression(self, expr: ExpressionSyntax) -> int:
        # we need to deal with Binary expressions and number expressions now
        if isinstance(expr, NumberExpressionSyntax):
            return expr.numberToken.value
        elif isinstance(expr, BinaryExpressionSyntax):
            left = self.EvaluateExpression(expr.left)
            right = self.EvaluateExpression(expr.right)
            switcher = {
                SyntaxKind.addition: left+right,
                SyntaxKind.subtraction: left-right,
                SyntaxKind.multiplication: left*right,
                SyntaxKind.division: left/right,
            }
            return switcher.get(expr.operatorToken.kind(), 0)
        elif isinstance(expr, ParanthesizedExpressionSyntax):
            return self.EvaluateExpression(expr.expression)
            

class BadBinaryExpressionOperatorException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """
    pass

class UnexpectedBinaryExpressionNodeException(Exception):
    """Exception thrown when an invalid operator is found in a Binary Expression
    """
    pass
