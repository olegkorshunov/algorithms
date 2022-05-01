import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_isEmpty(self):
        print(self.stack.is_empty())
        self.assertEqual(self.stack.is_empty(), True)

    def test_push(self):
        self.stack.push("(")
        self.stack.push(")")
        self.assertEqual(self.stack.is_empty(), False)

    def test_pop(self):
        self.stack.push("(")
        self.stack.push(")")
        self.assertEqual(self.stack.pop(), ")")

    def tearDown(self) -> None:
        del self.stack


if __name__ == "__main__":
    unittest.main()
