from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.parser import Parser


class TestParser:
    def test_peek(self, parser_simple: Parser) -> None:
        assert parser_simple.peek(0).kind() == SyntaxKind.literal
        assert parser_simple.peek(1).kind() == SyntaxKind.addition
        assert parser_simple.peek(2).kind() == SyntaxKind.literal
        assert parser_simple.peek(3).kind() == SyntaxKind.endoffile
        assert parser_simple.peek(4).kind() == SyntaxKind.endoffile

    def test_current(self, parser_simple: Parser) -> None:
        assert parser_simple.current().kind() == SyntaxKind.literal
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.addition
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.literal
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.endoffile

    def test_matchToken(self, parser_simple: Parser) -> None:
        token = parser_simple.match_token(SyntaxKind.endoffile)
        assert token.kind() == SyntaxKind.endoffile
        expected_error = filter(
            lambda d: d.startswith(
                "ERROR: Parser:Matchoken: unexpected token, Expected"
            ),
            parser_simple.diagnostics,
        )
        # assert len(expected_error) == 1

    def test_parse_simple(self) -> None:
        parser = Parser("2+3", 0)
        assert parser.current().kind() == SyntaxKind.literal
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.addition
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.literal
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.endoffile

    def test_parsePrimaryExpression_simple(self) -> None:
        parser = Parser("2+3", 0)
        literal_expression_syntax = parser.parse_primary_expression()
        assert literal_expression_syntax.kind() == SyntaxKind.literal
        assert literal_expression_syntax.literal_token.value == 2

