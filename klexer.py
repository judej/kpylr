from typing import List
from knode import SyntaxToken, SyntaxKind


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

    def nextToken(self) -> SyntaxToken:
        """Returns the next Syntax token. Currently only supports  +, -, *, /, (, ), <whitespace>

        :raises LexerExceptionBadToken: [description]
        :return: [description]
        :rtype: SyntaxToken
        """
        # looking for +, -, *, /, (, ), .whitespace
        if self.position >= len(self.text):
            return SyntaxToken("\0", self.current(), SyntaxKind.endoffile, "\0")

        if self.current().isnumeric():
            start = self.position
            while self.current().isnumeric():
                self.next()
            length = self.position - start
            tokentext = self.text[start : start + length]
            tokenvalue = 0
            try:
                tokenvalue = int(tokentext)
            except ValueError as ex:
                self.diagnostics.append(f"ERROR: the token {tokentext} cannot be represented as an int")

            return SyntaxToken(tokentext, start, SyntaxKind.number, tokenvalue)

        if self.current().isalpha():
            start = self.position
            while self.current().isalpha():
                self.next()
            length = self.position - start
            tokentext = self.text[start : start + length]
            return SyntaxToken(tokentext, start, SyntaxKind.string, tokentext)

        if self.current().isspace():
            start = self.position
            while self.current().isspace():
                self.next()
            length = self.position - start
            tokentext = self.text[start : start + length]
            return SyntaxToken(tokentext, start, SyntaxKind.whitespace, tokentext)

        if self.current() == "+":
            self.next()
            return SyntaxToken("+", self.position - 1, SyntaxKind.addition, None)
        elif self.current() == "-":
            self.next()
            return SyntaxToken("-", self.position - 1, SyntaxKind.subtraction, None)
        elif self.current() == "*":
            self.next()
            return SyntaxToken("*", self.position - 1, SyntaxKind.multiplication, None)
        elif self.current() == "/":
            self.next()
            return SyntaxToken("/", self.position - 1, SyntaxKind.division, None)
        elif self.current() == "(":
            self.next()
            return SyntaxToken("(", self.position - 1, SyntaxKind.openparanthesis, None)
        elif self.current() == ")":
            self.next()
            return SyntaxToken(
                ")", self.position - 1, SyntaxKind.closeparanthesis, None
            )
        else:
            self.diagnostics.append(f"ERROR: bad character in input: {self.current()}")
            raise LexerExceptionBadToken()

        self.next()
        return SyntaxToken(
            self.text[self.position - 1 : self.position],
            self.current(),
            SyntaxKind.badtoken,
            None,
        )

    def current(self) -> str:
        """returns the character at the current position. '\0' if at end of the string

        :return: [description]
        :rtype: str
        """
        if self.position >= len(self.text):
            return '\0'
        return self.text[self.position]

    def next(self) -> None:
        """Move the current position to the next character
        """
        self.position += 1

class LexerExceptionBadToken(Exception):
    """Exception thrown when a lexed token is bad
    """
    pass
