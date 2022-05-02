class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return True if len(self._stack) == 0 else False

    def clear(self):
        self._stack.clear()

    def peek(self):
        return self._stack[-1]
