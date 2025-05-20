"""
This module provides a simple function to add two integers.
"""


def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b


if __name__ == "__main__":
    print(add(20, 30))
