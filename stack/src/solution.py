from .stack import Stack


class IsBracesSequenceCorrect:
    def __init__(self, braces: tuple):
        """
        braces - tuple of opening brackets,
        for example ('(','[','{',)
        """
        self.stack = Stack()
        self.braces = braces

    def __call__(self, string: str) -> bool:
        for s in string:
            if s in self.braces and self.stack.is_empty():
                self.stack.push(s)
