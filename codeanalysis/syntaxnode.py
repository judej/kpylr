from abc import ABC, abstractmethod
from codeanalysis.syntaxkind import SyntaxKind
from typing import Any, List

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
