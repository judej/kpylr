from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax
from typing import Any, List


class ParanthesizedExpressionSyntax(ExpressionSyntax):
    def __init__(
        self, openParansToken: SyntaxToken, expression: ExpressionSyntax, closeParansToken: SyntaxToken,
    ) -> None:
        self.openParansToken = openParansToken
        self.expression = expression
        self.closeParansToken = closeParansToken

    def kind(self):
        return SyntaxKind.paranthesizedexpression

    def get_children(self) -> List[SyntaxNode]:
        """returns the children of a binary expression 

        :return: iterable of left, operator and right of the binary expression
        :rtype: List[SyntaxNode]
        :rtype: Iterator[List[SyntaxNode]]
        """
        yield self.openParansToken
        yield self.expression
        yield self.closeParansToken

    def get_last_child(self) -> SyntaxNode:
        return self.closeParansToken
