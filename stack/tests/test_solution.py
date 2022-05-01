import unittest
from src.solution import IsBracesSequenceCorrect


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.correct = [
            "[]",
            "[({})]",
            "({()}[()])",
            "({(([()]))}[{}]())",
            "{{}}()()()()",
        ]
        self.incorrect = [
            "[",
            ")",
            "([)]",
            "({}))",
            "({()})[(()]",
            "((){}()",
            "((()[))",
        ]
        self.is_this_correct = IsBracesSequenceCorrect(
            braces=(
                "(",
                "[",
                "{",
            )
        )


if __name__ == "__main__":
    unittest.main()