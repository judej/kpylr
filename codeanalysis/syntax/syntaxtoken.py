from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from typing import Any, Iterator, Union


class SyntaxToken(SyntaxNode):
    """Base class for all Syntax Tokens
    """

    def __init__(self, text: Union[str, None], position: int, kind: SyntaxKind, value: Any) -> None:
        """Create a Syntax token

        :text: The line to be tokenized
        :position: position of the token in the line
        :kind: the kind of syntax token
        :value: The value of the token - could be a string or literal etc
        """
        self.text = text
        self.position = position
        self.tokenkind = kind
        self.value = value
        return

    def get_children(self) -> Union[Iterator[SyntaxNode], Iterator[None]]:
        yield None

    @property
    def kind(self) -> SyntaxKind:
        return self.tokenkind

    def get_last_child(self) -> Union[SyntaxNode, None]:
        return None

