from codeanalysis.syntax.unaryexpressionsyntax import UnaryExpressionSyntax
from codeanalysis.syntax.syntaxfacts import SyntaxFacts
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax
from codeanalysis.syntax.syntaxtree import SyntaxTree
from codeanalysis.syntax.paranthesizedexpressionsyntax import ParanthesizedExpressionSyntax
from codeanalysis.syntax.lexer import Lexer
from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.literalexpressionsyntax import LiteralExpressionSyntax
from codeanalysis.syntax.binaryexpressionsyntax import BinaryExpressionSyntax


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
            if (token.kind() != SyntaxKind.badtoken) and (token.kind() != SyntaxKind.whitespacetoken):
                self.tokens.append(token)
            if token.kind() == SyntaxKind.endoffiletoken:
                break
            token = lex.lex()

    def _peek(self, offset: int) -> SyntaxToken:
        if self.position + offset >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[self.position + offset]

    def current(self) -> SyntaxToken:
        return self._peek(0)

    def next_token(self) -> SyntaxToken:
        _current = self.current()
        self.position += 1
        return _current

    def _match_token(self, kind: SyntaxKind) -> SyntaxToken:
        if self.current().kind() == kind:
            return self.next_token()
        self.diagnostics.append(
            f"ERROR: Parser:Matchoken: unexpected token, Expected {kind}, found {self.current().kind()}"
        )
        return SyntaxToken(None, 0, kind, None)

    def parse(self) -> SyntaxTree:
        return SyntaxTree(self.diagnostics, self._parse_expression(), self._match_token(SyntaxKind.endoffiletoken),)

    def _parse_expression(self, parent_precedence: int = 0) -> ExpressionSyntax:
        unary_operator_precedence = SyntaxFacts.get_unary_operator_precedence(self.current().kind())

        if (unary_operator_precedence != 0) and (unary_operator_precedence >= parent_precedence):
            operator_token = self.next_token()
            operand = self._parse_expression(unary_operator_precedence)
            left = UnaryExpressionSyntax(operator_token, operand)
        else:
            left = self._parse_primary_expression()

        while True:
            precedence = SyntaxFacts.get_binary_operator_precedence(self.current().kind())
            if (precedence == 0) or (precedence <= parent_precedence):
                break
            operator_token = self.next_token()
            right = self._parse_expression(precedence)
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def _parse_primary_expression(self) -> ExpressionSyntax:
        if self.current().kind() == SyntaxKind.openparanthesistoken:
            left = self.next_token()
            expression = self._parse_expression()
            right = self._match_token(SyntaxKind.closeparanthesistoken)
            return ParanthesizedExpressionSyntax(left, expression, right)

        literal_token = self._match_token(SyntaxKind.numbertoken)
        return LiteralExpressionSyntax(literal_token)

