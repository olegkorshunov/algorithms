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
        self.braces = opn_braces + cls_braces
        self.opn_cls = dict(zip(opn_braces, cls_braces))

    def __call__(self, braces: str) -> bool:

        for brace in braces:
            if brace not in self.braces:
                continue
            if brace in self.opn_braces:
                self.stack.push(brace)
            elif self.stack.is_empty():
                return False
            else:
                opn_brace = self.stack.pop()
                if brace != self.opn_cls[opn_brace]:
                    self.stack.clear()
                    return False

        result = self.stack.is_empty()
        self.stack.clear()
        return result
