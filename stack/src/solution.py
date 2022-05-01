from .stack import Stack


class IsBracesSequenceCorrect:
    def __init__(self, opn_braces: tuple, cls_braces: tuple):
        """
        opn_braces - tuple of opening brackets
        cls_braces - tuple of closing brackets
        for example:
        opn_braces = ('(','[','{',)
        cls_braces = (')',']','}',)
        """
        self.stack = Stack()
        self.opn_braces = opn_braces
        self.cls_braces = cls_braces

    def __call__(self, braces: str) -> bool:
        pass
