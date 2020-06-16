from abc import ABC, abstractmethod
from codeanalysis.syntax.syntaxnode import SyntaxNode


class ExpressionSyntax(SyntaxNode, ABC):
    def __init__(self) -> None:
        return

    @property
    @abstractmethod
    def get_last_child(self) -> SyntaxNode:
        pass

