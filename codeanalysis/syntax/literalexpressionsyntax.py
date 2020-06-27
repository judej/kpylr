from typing import Iterator
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax


class LiteralExpressionSyntax(ExpressionSyntax):
    """ExpressionSyntax(Syntax Node) that is used for a literal expression e.g. '2' 
    :param ExpressionSyntax: ExpressionSyntax(SyntaxNode)
    """

    def __init__(self, literal_token: SyntaxToken) -> None:
        self.literal_token = literal_token
        return

    @property
    def kind(self) -> SyntaxKind:
        return SyntaxKind.numbertoken

    def get_children(self) -> Iterator[SyntaxNode]:
        yield self.literal_token

    def get_last_child(self) -> SyntaxNode:
        return self.literal_token
