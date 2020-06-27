from typing import Iterator
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax


class BinaryExpressionSyntax(ExpressionSyntax):
    """Binary expression syntax node that has a left SyntaxNode, an operator_token and a right syntax node
    """

    def __init__(self, left: ExpressionSyntax, operator_token: SyntaxToken, right: ExpressionSyntax,) -> None:
        """Constructor for BinaryExpressionSyntax - left, operator and right

        :param left: An expression Syntax (could be another Binary Expression)
        :param operator_token: Operator token 
        :param right: An expression Syntax (could be another Binary Expression)
        """
        self.left = left
        self.operator_token = operator_token
        self.right = right
        return

    @property
    def kind(self) -> SyntaxKind:
        return SyntaxKind.binaryexpression

    def get_children(self) -> Iterator[SyntaxNode]:
        """returns the children of a binary expression 

        :return: iterable of left, operator and right of the binary expression
        :rtype: List[SyntaxNode]
        :rtype: Iterator[List[SyntaxNode]]
        """
        yield self.left
        yield self.operator_token
        yield self.right

    def get_last_child(self) -> SyntaxNode:
        return self.right
