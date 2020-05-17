from klexer import Lexer
from ktoken import SyntaxKind
# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree

inputText = input('>')
lex = Lexer(inputText)
token = lex.nextToken()
while (token.kind != SyntaxKind.endoffile) and \
    (token.kind != SyntaxKind.badtoken):
    print('text: "{}", kind: {}, value: {}'.format(token.text, token.kind, token.value))
    token = lex.nextToken()

