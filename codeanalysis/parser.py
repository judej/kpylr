from codeanalysis.syntaxtree import SyntaxTree
from codeanalysis.node import BinaryExpressionSyntax, ExpressionSyntax, NumberExpressionSyntax, ParanthesizedExpressionSyntax
from codeanalysis.lexer import Lexer
from codeanalysis.node import SyntaxToken, SyntaxKind

class Parser:
    tokens = []
    diagnostics = []
    def __init__(self, text: str, position: int) -> None:
        self.text = text
        self.position = position

        lex = Lexer(text)
        if(len(lex.diagnostics)>0):
            self.diagnostics.append(lex.diagnostics)
        token = lex.nextToken()

        while True:
            if (token.kind() != SyntaxKind.badtoken) and \
               (token.kind() != SyntaxKind.whitespace):
               self.tokens.append(token)
            if token.kind() == SyntaxKind.endoffile:
                break
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
        if self.current().kind() == kind:
            return self.nextToken()
        self.diagnostics.append(f"ERROR: Parser:Matchoken: unexpected token, Expected {kind}, found {self.current().kind()}")
        return SyntaxToken(None, 0, kind, None)

    def parseexpression(self) -> ExpressionSyntax:
        return self.parseterm()


    def parse(self) -> SyntaxTree:
        return SyntaxTree(self.diagnostics, self.parseterm(), self.matchToken(SyntaxKind.endoffile))
    
    def parseterm(self) -> ExpressionSyntax:
        left = self.parsefactor()
        while (self.current().kind() == SyntaxKind.addition) or \
            (self.current().kind() == SyntaxKind.subtraction):
            operatorToken = self.nextToken()
            right = self.parsefactor()
            left = BinaryExpressionSyntax(left, operatorToken, right)

        return left

    def parsefactor(self) -> ExpressionSyntax:
        left = self.parseprimaryexpression()
        while (self.current().kind() == SyntaxKind.division) or \
            (self.current().kind() == SyntaxKind.multiplication):
            operatorToken = self.nextToken()
            right = self.parseprimaryexpression()
            left = BinaryExpressionSyntax(left, operatorToken, right)
        return left

    def parseprimaryexpression(self) -> ExpressionSyntax:
        if self.current().kind() == SyntaxKind.openparanthesis:
            left = self.nextToken()
            expression = self.parseexpression()
            right = self.matchToken(SyntaxKind.closeparanthesis)
            return ParanthesizedExpressionSyntax(left, expression, right)

        numberToken = self.matchToken(SyntaxKind.number)
        return NumberExpressionSyntax(numberToken)






            

