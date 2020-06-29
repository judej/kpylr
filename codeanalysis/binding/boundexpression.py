from abc import ABCMeta
from codeanalysis.binding.boundnodekind import BoundNodeKind


class BoundExpression(BoundNodeKind, ABCMeta):
    pass
