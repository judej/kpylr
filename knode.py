from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, List

class SyntaxKind(Enum):
    number = 1,
    string = 2,
    addition = 3,
    subtraction = 4, 
    multiplication = 5,
    division = 6,
    whitespace = 7,
    openparanthesis = 8,
    closeparanthesis = 9,
    endoffile = 10,
    badtoken = 11,
    binaryexpression = 12,

class SyntaxNode(ABC):
    def __init__(cls) -> None:
        return
    
    @property
    @abstractmethod
    def kind(self) -> SyntaxKind: pass

    @property
    @abstractmethod
    def getChildren(self) -> List[Any]: pass

class SyntaxToken(SyntaxNode):
    def __init__(cls, text: str, position: int, kind: SyntaxKind, value: Any) -> None:
        cls.text = text
        cls.position = position
        cls.kind = kind
        cls.value = value

        return

    def getChildren(self) -> List[SyntaxNode]: 
        yield None

    def kind(self) -> SyntaxKind:
        return self.kind          

class ExpressionSyntax(SyntaxNode):
    def __init__(cls) -> None:
        return

class NumberExpressionSyntax(ExpressionSyntax):
    def __init__(cls, numberToken:SyntaxToken) -> None:
        cls.numberToken = numberToken
        return
    
    def kind(self):
        return SyntaxKind.number
    
    def getChildren(self) -> List[SyntaxNode]: 
         yield self.numberToken

class BinaryExpressionSyntax(ExpressionSyntax):

    def __init__(cls, left: ExpressionSyntax, operatorToken:SyntaxToken, right: ExpressionSyntax )-> None:
        cls.left = left
        cls.operatorToken = operatorToken
        cls.right = right
        return
    
    def kind(self):
        return SyntaxKind.binaryexpression
    
    def getChildren(self) -> List[SyntaxNode]: 
         yield self.operatorToken
         yield self.left
         yield self.right
