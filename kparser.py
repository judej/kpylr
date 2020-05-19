from knode import BinaryExpressionSyntax, ExpressionSyntax, NumberExpressionSyntax
from klexer import Lexer
from knode import SyntaxToken, SyntaxKind

class Parser:
    tokens = []
    def __init__(cls, text: str, position: int) -> None:
        cls.text = text
        cls.position = position

        lex = Lexer(text)
        token = lex.nextToken()

        while token.kind != SyntaxKind.endoffile:
            if (token.kind != SyntaxKind.badtoken) and \
               (token.kind != SyntaxKind.whitespace):
               cls.tokens.append(token)
            token = lex.nextToken()

    def peek(self, offset: int) -> SyntaxToken:
        if(self.position + offset >= len(self.tokens)):
            return self.tokens[-1]
        
        return self.tokens[self.position+offset]

    def current(self) -> SyntaxToken:
        return self.peek(0)
    
    def nextToken(self) -> SyntaxToken:
        _current = self.current()
        self.position += 1
        return _current
        
    def matchToken(self, kind: SyntaxKind) -> SyntaxToken:
        if self.current().kind == kind:
            return self.nextToken()
        return SyntaxToken(None, self.current().postion, kind, None)

    def parse(self) -> ExpressionSyntax:
        primary = None
        left = self.parsePrimaryExpression()
        while (self.current().kind == SyntaxKind.addition) or \
            (self.current().kind == SyntaxKind.subtraction):
            operatorToken = self.nextToken()
            right = self.parsePrimaryExpression()
            left = BinaryExpressionSyntax(left, operatorToken, right)

        return left

    def parsePrimaryExpression(self) -> ExpressionSyntax:
        numberToken = self.matchToken(SyntaxKind.number)
        return NumberExpressionSyntax(numberToken)






            

