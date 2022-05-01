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
            "(2+3)*(2*[4+3])/{7*8^(.5)}",
        ]
        self.incorrect = [
            "[",
            ")",
            "([)]",
            "({}))",
            "({()})[(()]",
            "((){}()",
            "((()[))",
            "(2+3)/{4-8",
        ]
        self.is_this_correct = IsBracesSequenceCorrect(
            opn_braces=("(", "[", "{"),
            cls_braces=(")", "]", "}"),
        )


if __name__ == "__main__":
    unittest.main()
