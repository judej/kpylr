from typing import List
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.syntaxnode import SyntaxNode
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.expressionsyntax import ExpressionSyntax


class UnaryExpressionSyntax(ExpressionSyntax):
    """
    """

    def __init__(self, operator_token: SyntaxToken, operand: ExpressionSyntax,) -> None:
        self.operator_token = operator_token
        self.operand = operand
        return

    def kind(self):
        return SyntaxKind.unaryexpression

    def get_children(self) -> List[SyntaxNode]:
        yield self.operator_token
        yield self.operand

    def get_last_child(self) -> SyntaxNode:
        return self.operand
