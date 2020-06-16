import pytest
from codeanalysis.syntax.expressionsyntax import ExpressionSyntax


class TestExpressionSyntax:
    def test_creation(self):
        with pytest.raises(Exception) as excinfo:
            expressionSyntax = ExpressionSyntax()
        assert (
            str(excinfo.value)
            == "Can't instantiate abstract class ExpressionSyntax with abstract methods get_children, get_last_child, kind"
        )
