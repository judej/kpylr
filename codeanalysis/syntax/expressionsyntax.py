from abc import ABC, abstractmethod
from typing import Iterator
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.syntaxnode import SyntaxNode


class ExpressionSyntax(SyntaxNode, ABC):
    def __init__(self) -> None:
        return

    @property
    @abstractmethod
    def kind(self) -> SyntaxKind:
        """Every derived class must state what kind of token it is.
        """
        pass

    @abstractmethod
    def get_children(self) -> Iterator[SyntaxNode]:
        pass

    @abstractmethod
    def get_last_child(self) -> SyntaxNode:
        pass

