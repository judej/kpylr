import pytest
from ..node import SyntaxKind
from ..lexer import Lexer, LexerExceptionBadToken


class TestLexer:
    input1 = "3+4+5"
    badInputs = ["3~4*5", "2&1"]
    input3 = "(3+4)*5"

    def test_next_token_simple(self):
        lexer = Lexer(self.input1)
        assert lexer.next_token().value == 3
        assert lexer.next_token().text == "+"
        assert lexer.next_token().value == 4
        assert lexer.next_token().text == "+"
        assert lexer.next_token().value == 5

    @pytest.mark.parametrize(
        "input",
        [
            "3~4*5",
            "2!1",
            "2`3",
            "2@3",
            "2#3",
            "2$3",
            "2%3",
            "2_3",
            "2?3",
            "2.3",
            "2>3",
            "2<3",
            "2,3",
            "2|3",
            "2{3",
            "2}3",
            "2[3",
            "2]3",
            "2=3",
        ],
    )
    def test_next_token_bad(self, input):
        lexer = Lexer(input)
        with pytest.raises(LexerExceptionBadToken):
            token = lexer.next_token()
            while token.kind() != SyntaxKind.endoffile:
                token = lexer.next_token()

    def test_current(self):
        lexer = Lexer("a+b")
        assert lexer.current() == "a"
        lexer.next()
        assert lexer.current() == "+"
        lexer.next()
        assert lexer.current() == "b"
        lexer.next()
        assert lexer.current() == "\0"

