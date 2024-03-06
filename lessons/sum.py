"""Summing the elements of a list using different loops."""

__author__ = "730403386"


def w_sum(vals: list[float]) -> float:
    """Sums up elements of list using while loop."""
    total = 0.0
    idx = 0
    while idx < len(vals):
        value = vals[idx]
        total += value
        idx += 1
    return float(total)


def f_sum(vals: list[float]) -> float:
    """Sums up elements of list using for loop."""
    total_vals = 0.0
    for elem in vals:
        total_vals += elem
    return float(total_vals)


def f_range_sum(vals: list[float]) -> float:
    """Sums up elements of list using for in range loop."""
    vals_total = 0.0
    for index in range(0, len(vals)):
        vals_total += vals[index]
    return float(vals_total)


def sum(elements: list[int]) -> int:
    """Sum all elements in elements."""
    total: int = 0
    for elem in elements: 
        total += elem
    return total