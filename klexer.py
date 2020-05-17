from ktoken import SyntaxToken, SyntaxKind

class Lexer:
    def __init__(cls, text: str):
        cls.text = text 
        cls.position = 0

    def nextToken(self) -> SyntaxToken:
        # looking for +, -, *, /, (, ), .whitespace
        if  self.position >= len(self.text):
            return SyntaxToken('\0', self.current(), SyntaxKind.endoffile, '\0')

        if self.current().isnumeric():
            start = self.position
            while self.current().isnumeric():
                self.next()
            length = self.position - start
            tokentext = self.text[start: start+length]
            tokenvalue = int(tokentext)
            return SyntaxToken(tokentext, start, SyntaxKind.number, tokenvalue)
            
        if self.current().isalpha():
            start = self.position
            while self.current().isalpha():
                self.next()
            length = self.position - start
            tokentext = self.text[start: start+length]
            return SyntaxToken(tokentext, start, SyntaxKind.string, tokentext)

        if self.current().isspace():
            start = self.position
            while self.current().isspace():
                self.next()
            length = self.position - start
            tokentext = self.text[start: start+length]
            return SyntaxToken(tokentext, start, SyntaxKind.whitespace, tokentext)

        if self.current() == '+':
            self.next()
            return SyntaxToken('+', self.position-1, SyntaxKind.addition, None)
        if self.current() == '-':
            self.next()
            return SyntaxToken('-', self.position-1, SyntaxKind.subtraction, None)
        if self.current() == '*':
            self.next()
            return SyntaxToken('*', self.position-1, SyntaxKind.multiplication, None)
        if self.current() == '/':
            self.next()
            return SyntaxToken('/', self.position-1, SyntaxKind.division, None)
        if self.current() == '(':
            self.next()
            return SyntaxToken('(', self.position-1, SyntaxKind.openparanthesis, None)
        if self.current() == ')':
            self.next()
            return SyntaxToken(')', self.position-1, SyntaxKind.closeparanthesis, None)

        return SyntaxToken(self.text[self.position:self.position+1], self.current(), SyntaxKind.badtoken, None)
    
    def current(self) -> str:
        if self.position >= len(self.text):
            return '\0'
        return self.text[self.position]

    def next(self) -> None:
        self.position += 1

    def dump(self) -> str:
        return self.text

