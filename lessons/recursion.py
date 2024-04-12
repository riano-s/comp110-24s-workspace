"""Writing a recursive function."""

__author__ = "730403386"


# Recursive definition
def f(n: int, k: int) -> int:
    """Multiples value of n by the value of k."""
    if n == 0:  # base case
        return 0
    else:  # recrusive rule
        return f(n - 1, k) + k