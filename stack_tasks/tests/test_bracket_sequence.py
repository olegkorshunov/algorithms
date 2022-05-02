import unittest
from bracket_sequence.solution import IsBracesSequenceCorrect


class TestIsBracesSequenceCorrect(unittest.TestCase):
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

    def test_correct(self):
        for braces in self.correct:
            print(f"Checked {braces}")
            self.assertEqual(self.is_this_correct(braces), True)

    def test_incorrect(self):
        for braces in self.incorrect:
            print(f"Checked {braces}")
            self.assertEqual(self.is_this_correct(braces), False)


if __name__ == "__main__":
    unittest.main()
