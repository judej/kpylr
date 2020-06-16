from codeanalysis.syntaxkind import SyntaxKind
from codeanalysis.parser import Parser


class TestParser:
    def test_peek(self, parser_simple: Parser) -> None:
        assert parser_simple._peek(0).kind() == SyntaxKind.numbertoken
        assert parser_simple._peek(1).kind() == SyntaxKind.additiontoken
        assert parser_simple._peek(2).kind() == SyntaxKind.numbertoken
        assert parser_simple._peek(3).kind() == SyntaxKind.endoffiletoken
        assert parser_simple._peek(4).kind() == SyntaxKind.endoffiletoken

    def test_current(self, parser_simple: Parser) -> None:
        assert parser_simple.current().kind() == SyntaxKind.numbertoken
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.additiontoken
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.numbertoken
        parser_simple.next_token()
        assert parser_simple.current().kind() == SyntaxKind.endoffiletoken

    def test_matchToken(self, parser_simple: Parser) -> None:
        token = parser_simple._match_token(SyntaxKind.endoffiletoken)
        assert token.kind() == SyntaxKind.endoffiletoken
        expected_error = filter(
            lambda d: d.startswith(
                "ERROR: Parser:Matchoken: unexpected token, Expected"
            ),
            parser_simple.diagnostics,
        )
        # assert len(expected_error) == 1

    def test_parse_simple(self) -> None:
        parser = Parser("2+3", 0)
        assert parser.current().kind() == SyntaxKind.numbertoken
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.additiontoken
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.numbertoken
        parser.next_token()
        assert parser.current().kind() == SyntaxKind.endoffiletoken

    def test_parsePrimaryExpression_simple(self) -> None:
        parser = Parser("2+3", 0)
        literal_expression_syntax = parser._parse_primary_expression()
        assert literal_expression_syntax.kind() == SyntaxKind.numbertoken
        assert literal_expression_syntax.literal_token.value == 2

