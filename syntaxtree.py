from node import ExpressionSyntax, SyntaxToken
from typing import List


class SyntaxTree:
    def __init__(self, diagnostics: List[str], root: ExpressionSyntax, endOfFileToken: SyntaxToken) -> None:
        self.diagnostics = diagnostics
        self.root = root
        self. endOfFileToken = endOfFileToken

