from kparser import Parser
from knode import SyntaxNode, SyntaxToken, SyntaxKind

# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree
# ├── a-first.html
# ├── b-second.html
# ├── subfolder
# │   ├── rea

def prettyPrint(node: SyntaxNode, indent: str = '') -> None:
    
    if isinstance(node, SyntaxToken):
        operator = (node.kind == SyntaxKind.addition) or (node.kind == SyntaxKind.subtraction) or \
            (node.kind == SyntaxKind.division) or (node.kind == SyntaxKind.multiplication) 
        branch = "" if operator else "├──"
        print('{}{}{}, value: {}'.format(indent, branch, node.kind, node.value))
        if operator: 
            indent += "    " 
    
    if hasattr(node, 'getChildren'):
        for child in node.getChildren():
            prettyPrint(child, indent)
    return

inputText = input('>')
parser = Parser(inputText,0)
expression = parser.parse()
prettyPrint(expression)


