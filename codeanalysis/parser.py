from codeanalysis.expressionsyntax import ExpressionSyntax
from codeanalysis.syntaxtree import SyntaxTree
from codeanalysis.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax
from codeanalysis.lexer import Lexer
from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.literalexpressionsyntax import LiteralExpressionSyntax
from codeanalysis.binaryexpressionsyntax import BinaryExpressionSyntax


class Parser:
    def __init__(self, text: str, position: int) -> None:
        self.text = text
        self.position = position
        self.tokens = []
        self.diagnostics = []

        lex = Lexer(text)
        if len(lex.diagnostics) > 0:
            self.diagnostics.append(lex.diagnostics)
        token = lex.lex()

        while True:
            if (token.kind() != SyntaxKind.badtoken) and (
                token.kind() != SyntaxKind.whitespacetoken
            ):
                self.tokens.append(token)
            if token.kind() == SyntaxKind.endoffiletoken:
                break
            token = lex.lex()

    def peek(self, offset: int) -> SyntaxToken:
        if self.position + offset >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[self.position + offset]

    def current(self) -> SyntaxToken:
        return self.peek(0)

    def next_token(self) -> SyntaxToken:
        _current = self.current()
        self.position += 1
        return _current

    def match_token(self, kind: SyntaxKind) -> SyntaxToken:
        if self.current().kind() == kind:
            return self.next_token()
        self.diagnostics.append(
            f"ERROR: Parser:Matchoken: unexpected token, Expected {kind}, found {self.current().kind()}"
        )
        return SyntaxToken(None, 0, kind, None)

    def parse(self) -> SyntaxTree:
        return SyntaxTree(
            self.diagnostics,
            self.parse_expression(),
            self.match_token(SyntaxKind.endoffiletoken),
        )

    def parse_expression(self) -> ExpressionSyntax:
        return self.parse_term()

    def parse_term(self) -> ExpressionSyntax:
        left = self.parse_factor()
        while (self.current().kind() == SyntaxKind.additiontoken) or (
            self.current().kind() == SyntaxKind.subtractiontoken
        ):
            operator_token = self.next_token()
            right = self.parse_factor()
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def parse_factor(self) -> ExpressionSyntax:
        left = self.parse_primary_expression()
        while (self.current().kind() == SyntaxKind.divisiontoken) or (
            self.current().kind() == SyntaxKind.multiplicationtoken
        ):
            operator_token = self.next_token()
            right = self.parse_primary_expression()
            left = BinaryExpressionSyntax(left, operator_token, right)
        return left

    def parse_primary_expression(self) -> ExpressionSyntax:
        if self.current().kind() == SyntaxKind.openparanthesistoken:
            left = self.next_token()
            expression = self.parse_expression()
            right = self.match_token(SyntaxKind.closeparanthesistoken)
            return ParanthesizedExpressionSyntax(left, expression, right)

        literal_token = self.match_token(SyntaxKind.numbertoken)
        return LiteralExpressionSyntax(literal_token)

