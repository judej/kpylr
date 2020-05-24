from knode import SyntaxToken, SyntaxKind

class Lexer:
    '''[summary]

    :raises LexerExceptionBadToken: [description]
    :return: [description]
    :rtype: [type]
    '''
    def __init__(cls, text: str):
        cls.text = text 
        cls.position = 0

    def nextToken(self) -> SyntaxToken:
        '''[summary]

        :raises LexerExceptionBadToken: [description]
        :return: [description]
        :rtype: SyntaxToken
        '''
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
        elif self.current() == '-':
            self.next()
            return SyntaxToken('-', self.position-1, SyntaxKind.subtraction, None)
        elif self.current() == '*':
            self.next()
            return SyntaxToken('*', self.position-1, SyntaxKind.multiplication, None)
        elif self.current() == '/':
            self.next()
            return SyntaxToken('/', self.position-1, SyntaxKind.division, None)
        elif self.current() == '(':
            self.next()
            return SyntaxToken('(', self.position-1, SyntaxKind.openparanthesis, None)
        elif self.current() == ')':
            self.next()
            return SyntaxToken(')', self.position-1, SyntaxKind.closeparanthesis, None)
        else:
            raise LexerExceptionBadToken()


        self.next()
        return SyntaxToken(self.text[self.position-1:self.position], self.current(), SyntaxKind.badtoken, None)
    
    def current(self) -> str:
        '''[summary]

        :return: [description]
        :rtype: str
        '''
        if self.position >= len(self.text):
            return '\0'
        return self.text[self.position]

    def next(self) -> None:
        '''[summary]
        '''
        self.position += 1

    def dump(self) -> str:
        '''[summary]

        :return: [description]
        :rtype: str
        '''
        return self.text

class LexerExceptionBadToken(Exception):
    '''Exception thrown when a lexed token is bad
    '''
    pass