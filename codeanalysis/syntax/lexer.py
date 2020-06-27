from codeanalysis.syntax.syntaxtoken import SyntaxToken
from codeanalysis.syntax.syntaxkind import SyntaxKind


class Lexer:
    """[summary]

    :raises LexerExceptionBadToken: [description]
    :return: [description]
    :rtype: [type]
    """

    diagnostics = []

    def __init__(self, text: str):
        self.text = text
        self.position = 0

    def lex(self) -> SyntaxToken:
        """Returns the next Syntax token. Currently only supports  +, -, *, /, (, ), <whitespace>

        :raises LexerExceptionBadToken: [description]
        :return: [description]
        :rtype: SyntaxToken
        """
        # looking for +, -, *, /, (, ), .whitespace
        if self.position >= len(self.text):
            return SyntaxToken("\0", self.position, SyntaxKind.endoffiletoken, "\0")

        if self.current.isnumeric():
            start = self.position
            while self.current.isnumeric():
                self.next()
            length = self.position - start
            tokentext = self.text[start : start + length]
            tokenvalue = 0
            try:
                tokenvalue = int(tokentext)
            except ValueError:
                self.diagnostics.append(
                    f"ERROR: Lexer:NextToken: the token {tokentext} cannot be represented as an int"
                )

            return SyntaxToken(tokentext, start, SyntaxKind.numbertoken, tokenvalue)

        if self.current.isspace():
            start = self.position
            while self.current.isspace():
                self.next()
            length = self.position - start
            tokentext = self.text[start : start + length]
            return SyntaxToken(tokentext, start, SyntaxKind.whitespacetoken, tokentext)

        if self.current == "+":
            self.next()
            return SyntaxToken("+", self.position - 1, SyntaxKind.additiontoken, None)
        elif self.current == "-":
            self.next()
            return SyntaxToken("-", self.position - 1, SyntaxKind.subtractiontoken, None)
        elif self.current == "*":
            self.next()
            return SyntaxToken("*", self.position - 1, SyntaxKind.multiplicationtoken, None)
        elif self.current == "/":
            self.next()
            return SyntaxToken("/", self.position - 1, SyntaxKind.divisiontoken, None)
        elif self.current == "(":
            self.next()
            return SyntaxToken("(", self.position - 1, SyntaxKind.openparanthesistoken, None)
        elif self.current == ")":
            self.next()
            return SyntaxToken(")", self.position - 1, SyntaxKind.closeparanthesistoken, None)
        else:
            self.diagnostics.append(f"ERROR: Lexer:NextToken: bad character in input: {self.current}")

        self.next()
        return SyntaxToken(self.text[self.position - 1 : self.position], self.position, SyntaxKind.badtoken, None,)

    @property
    def current(self) -> str:
        """returns the character at the current position. '\0' if at end of the string

        :return: [description]
        :rtype: str
        """
        if self.position >= len(self.text):
            return "\0"
        return self.text[self.position]

    def next(self) -> None:
        """Move the current position to the next character
        """
        self.position += 1


class LexerExceptionBadToken(Exception):
    """Exception thrown when a lexed token is bad
    """

    pass
