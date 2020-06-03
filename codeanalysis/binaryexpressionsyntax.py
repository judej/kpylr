from typing import List
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.syntaxnode import SyntaxNode
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.expressionsyntax import ExpressionSyntax


class BinaryExpressionSyntax(ExpressionSyntax):
    """Binary expression syntax node that has a left SyntaxNode, an operatorToken and a right syntax node
    """

    def __init__(
        self,
        left: ExpressionSyntax,
        operatorToken: SyntaxToken,
        right: ExpressionSyntax,
    ) -> None:
        """Constructor for BinaryExpressionSyntax - left, operator and right

        :param left: An expression Syntax (could be another Binary Expression)
        :param operatorToken: Operator token 
        :param right: An expression Syntax (could be another Binary Expression)
        """
        self.left = left
        self.operatorToken = operatorToken
        self.right = right
        return

    def kind(self):
        return SyntaxKind.binaryexpression

    def get_children(self) -> List[SyntaxNode]:
        """returns the children of a binary expression 

        :return: iterable of left, operator and right of the binary expression
        :rtype: List[SyntaxNode]
        :rtype: Iterator[List[SyntaxNode]]
        """
        yield self.left
        yield self.operatorToken
        yield self.right

    def get_last_child(self) -> SyntaxNode:
        return self.right