import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Tests addition of positive integers."""
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        """Tests addition of negative integers."""
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_sign_numbers(self):
        """Tests addition of integers with different signs."""
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        """Tests addition with zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_large_numbers(self):
        """Tests addition of large integer values."""
        self.assertEqual(add(10**9, 10**9), 2 * 10**9)

    def test_add_type_error(self):
        """Tests that TypeError is raised for non-integer inputs."""
        with self.assertRaises(TypeError):
            add("1", 2)
        with self.assertRaises(TypeError):
            add(1, "2")
        with self.assertRaises(TypeError):
            add("1", "2")


if __name__ == "__main__":
    unittest.main(verbosity=2)
