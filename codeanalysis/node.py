from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, List


class SyntaxKind(Enum):
    """Kinds of Syntax Tokens
    """

    number = (1,)
    string = (2,)
    addition = (3,)
    subtraction = (4,)
    multiplication = (5,)
    division = (6,)
    whitespace = (7,)
    openparanthesis = (8,)
    closeparanthesis = (9,)
    badtoken = (10,)
    binaryexpression = (11,)
    paranthesizedexpression = (12,)
    endoffile = 13


class SyntaxNode(ABC):
    """Structure to support a Syntax Token Node. 
    :param ABC: Since this will be an abstract base class - inheriting from ABC
    """

    def __init__(self) -> None:
        return

    @property
    @abstractmethod
    def kind(self) -> SyntaxKind:
        pass

    """Every derived class must state what kind of token it is.
    """

    @property
    @abstractmethod
    def get_children(self) -> List[Any]:
        pass

    """A node may have children
    """


class SyntaxToken(SyntaxNode):
    """Base class for all Syntax Tokens
    """

    def __init__(self, text: str, position: int, kind: SyntaxKind, value: Any) -> None:
        """Create a Syntax token

        :text: The line to be tokenized
        :position: position of the token in the line
        :kind: the kind of syntax token
        :value: The value of the token - could be a string or number etc
        """
        self.text = text
        self.position = position
        self.tokenkind = kind
        self.value = value
        return

    def get_children(self) -> List[SyntaxNode]:
        yield None

    def kind(self) -> SyntaxKind:
        return self.tokenkind

    def get_last_child(self) -> SyntaxNode:
        return None


class ExpressionSyntax(SyntaxNode, ABC):
    def __init__(self) -> None:
        return

    @property
    @abstractmethod
    def get_last_child(self) -> SyntaxNode:
        pass


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


class ParanthesizedExpressionSyntax(ExpressionSyntax):
    def __init__(
        self,
        openParansToken: SyntaxToken,
        expression: ExpressionSyntax,
        closeParansToken: SyntaxToken,
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
