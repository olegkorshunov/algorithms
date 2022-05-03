import unittest
from stack.stack import Stack
from stack.stack import PopFromEmptyStack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_isEmpty(self):
        self.assertEqual(self.stack.isEmpty(), True)

    def test_push(self):
        self.stack.push("(")
        self.stack.push(")")
        self.assertEqual(self.stack.isEmpty(), False)

    def test_pop(self):
        self.stack.push("(")
        self.stack.push(")")
        self.assertEqual(self.stack.pop(), ")")

    def test_pop_from_empty(self):
        with self.assertRaises(PopFromEmptyStack):
            self.stack.pop()

    def tearDown(self) -> None:
        del self.stack


if __name__ == "__main__":
    unittest.main()
