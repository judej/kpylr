from codeanalysis.evaluator import Evaluator
from codeanalysis.syntax.syntaxtree import SyntaxTree
from codeanalysis.syntax.parser import Parser
from codeanalysis.syntax.syntaxnode import SyntaxNode
from codeanalysis.syntax.syntaxkind import SyntaxKind
from codeanalysis.syntax.syntaxtoken import SyntaxToken

# minimal compiler
# Take input
# lexer => tokens -> dump()-> list of tokens
# parser => expression trees dump() -> expression tree
# ├── readme.html
# │   ├── code.cpp
# │   └── code.h


def pretty_print(node: SyntaxNode, indent: str = "", isLast: bool = True) -> None:
    if not node:
        return

    marker = "└──" if isLast else "├──"

    if isinstance(node, SyntaxToken) and (node.value):
        print(f'{indent}{marker}{node.kind()}{"  "}{node.value}')
    else:
        print(f"{indent}{marker}{node.kind()}")

    indent += "    " if isLast else "│    "

    lastChild = node.get_last_child()

    for child in node.get_children():
        pretty_print(child, indent, child == lastChild)


while True:
    inputText = input(">")
    parser = Parser(inputText, 0)
    syntax_tree = parser.parse()
    pretty_print(syntax_tree.root)
    if len(syntax_tree.diagnostics) > 0:
        print(syntax_tree.diagnostics)
    else:
        evaluator = Evaluator(syntax_tree.root)
        value = evaluator.evaluate()
        print(f"Result: {value}")
