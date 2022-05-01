import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.correct = [
            "[]",
            "[({})]",
            "({()}[()])",
            "({(([()]))}[{}]())",
            "{{}}()()()()",
        ]


if __name__ == "__main__":
    unittest.main()
