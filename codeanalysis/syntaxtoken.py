from codeanalysis.syntaxnode import SyntaxNode
from codeanalysis.syntaxkind import SyntaxKind
from typing import Any, List

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

