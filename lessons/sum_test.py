"""Test sum functionality."""

from lessons.sum import sum

def test_sum_empty() -> None:
    """Sum of empty list should return 0."""
    assert sum([]) == 0

def test_sum_one_element() -> None:
    """Sum of one """

def test_sum_positive() -> None:
    """Sum of positive numbers should return sum of these numbers."""
    test: list[int] = [2, 4, 6]
    assert sum(test) == 12