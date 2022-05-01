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
            opn_braces=("(", "[", "{"),
            cls_braces=(")", "]", "}"),
        )


if __name__ == "__main__":
    unittest.main()
