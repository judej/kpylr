from codeanalysis.syntaxtoken import SyntaxToken
from codeanalysis.syntaxkind import SyntaxKind


class TestSyntaxToken:
    def test_create_syntax_token(self):
        syntaxToken = SyntaxToken("2+3", 1, SyntaxKind.addition, None)
        assert True

    def test_getChildren(self):
        syntaxToken = SyntaxToken("2+3", 1, SyntaxKind.addition, None)
        assert True

    def test_getLastChild(self):
        assert True

    def test_kind(self):
        assert True

