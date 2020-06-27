from abc import ABC, abstractmethod
from codeanalysis.syntax.syntaxkind import SyntaxKind
from typing import Any, Iterator


class SyntaxNode(ABC):
    """Structure to support a Syntax Token Node. 
    :param ABC: Since this will be an abstract base class - inheriting from ABC
    """

    def __init__(self) -> None:
        return

    @property
    @abstractmethod
    def kind(self) -> SyntaxKind:
        """Every derived class must state what kind of token it is.
        """
        pass

    @abstractmethod
    def get_children(self) -> Iterator[Any]:
        """A node may have children
        """
        pass

    @abstractmethod
    def get_last_child(self) -> Any:
        pass
