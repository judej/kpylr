from kparser import Parser
from knode import SyntaxNode, SyntaxToken, SyntaxKind

# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree
# ├── readme.html
# │   ├── code.cpp
# │   └── code.h

def prettyPrint(node: SyntaxNode, indent: str = '', isLast:bool = False) -> None:
    marker = '└──' if isLast else '├──'
    print('{}{}{}'.format(indent, marker, node.kind))

    if isinstance(node, SyntaxToken):
        print('{}{}\r\n'.format('  ', node.value))
    
    indent += '    ' if isLast else '│    '

    lastChild = node.getLastChild()

    for child in node.getChildren():
        if isinstance(child, SyntaxNode):
            prettyPrint(child, indent, child == lastChild)
   

inputText = input('>')
parser = Parser(inputText,0)
expression = parser.parse()
prettyPrint(expression)


