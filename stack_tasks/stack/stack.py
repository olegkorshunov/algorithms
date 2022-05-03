class PopFromEmptyStack(Exception):
    """
    Can't pop item from empty stack
    """

    pass


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise PopFromEmptyStack
        return self._stack.pop()

    def isEmpty(self):
        return True if len(self._stack) == 0 else False

    def clear(self):
        self._stack.clear()

    def peek(self):
        return self._stack[-1]
