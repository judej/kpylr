# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree

inputText = input('>')
lex = Lexer(inputText)

print('You entered ', inputText)

