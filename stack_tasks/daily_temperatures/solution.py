from stack.stack import Stack
from typing import List


class DailyTemperature:
    def __init__(self):
        self.stack = Stack()

    def __call__(self, temperature: List[int]) -> List[int]:

        result = []
        for i in enumerate(temperature[::-1]):
            if self.stack.isEmpty():
                if self.stack.isEmpty():
                    self.stack.push(i)
                    result.append(0)
                elif i[1] <= self.stack.peek()[1]:
                    self.stack.push(i)
                    result.append(1)

            while i[1] >= self.stack.peek()[1]:
                self.stack.pop()
                if self.stack.isEmpty():
                    self.stack.push(i)
                    result.append(0)
                    break
            else:
                result.append(i[0] - self.stack.peek()[0])
                self.stack.push(i)

            self.stack.clear()
            return result[::-1]
