from typing import Union
import pytest
from codeanalysis.parser import Parser
from codeanalysis.evaluator import Evaluator


class TestEvaluator:

    testexpressions = [("2+3", 5), ("2-1", 1), ("2*2", 4), ("6/2", 3), ("(2+3)*5", 25)]

    @pytest.mark.parametrize("expr, result", testexpressions)
    def test_evaluate(self, expr: str, result: Union[int, float]) -> None:
        parser = Parser(expr, 0)
        syntaxtree = parser.parse()
        evaluator = Evaluator(syntaxtree.root)
        assert evaluator.evaluate() == result
