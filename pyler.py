from codeanalysis.evaluator import Evaluator
from codeanalysis.syntaxtree import SyntaxTree
from codeanalysis.parser import Parser
from codeanalysis.node import SyntaxNode, SyntaxToken, SyntaxKind

# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree
# ├── readme.html
# │   ├── code.cpp
# │   └── code.h

def prettyPrint(node: SyntaxNode, indent: str = '', isLast:bool = True) -> None:
    if not node:
        return

    marker = '└──' if isLast else '├──'

    if (isinstance(node, SyntaxToken) and (node.value)):
        print(f'{indent}{marker}{node.kind()}{"  "}{node.value}')
    else: 
        print(f'{indent}{marker}{node.kind()}')
    
    indent += '    ' if isLast else '│    '

    lastChild = node.getLastChild()

    for child in node.getChildren():
        prettyPrint(child, indent, child == lastChild)
   

while True:
    inputText = input('>')
    parser = Parser(inputText,0)
    syntaxTree = parser.parse()
    prettyPrint(syntaxTree.root)
    if len(syntaxTree.diagnostics) > 0:
        print(syntaxTree.diagnostics)
    else: 
        evaluator = Evaluator(syntaxTree.root)
        value = evaluator.Evaluate()
        print(f"Result: {value}")


