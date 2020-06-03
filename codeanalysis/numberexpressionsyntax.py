from typing import List
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.syntaxnode import SyntaxNode
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.expressionsyntax import ExpressionSyntax


class NumberExpressionSyntax(ExpressionSyntax):
    """ExpressionSyntax(Syntax Node) that is used for a number expression e.g. '2' 
    :param ExpressionSyntax: ExpressionSyntax(SyntaxNode)
    """

    def __init__(self, numberToken: SyntaxToken) -> None:
        self.numberToken = numberToken
        return

    def kind(self):
        return SyntaxKind.number

    def get_children(self) -> List[SyntaxNode]:
        yield self.numberToken

    def get_last_child(self) -> SyntaxNode:
        return self.numberToken
