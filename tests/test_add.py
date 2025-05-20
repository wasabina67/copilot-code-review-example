import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
