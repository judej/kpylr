from typing import Iterator
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax


class UnaryExpressionSyntax(ExpressionSyntax):
    """
    """

    def __init__(self, operator_token: SyntaxToken, operand: ExpressionSyntax,) -> None:
        self.operator_token = operator_token
        self.operand = operand
        return

    @property
    def kind(self) -> SyntaxKind:
        return SyntaxKind.unaryexpression

    @property
    def get_children(self) -> Iterator[SyntaxNode]:
        yield self.operator_token
        yield self.operand

    @property
    def get_last_child(self) -> SyntaxNode:
        return self.operand
