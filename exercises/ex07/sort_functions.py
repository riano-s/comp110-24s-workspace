"""Functions that implement sorting algorithms."""

__author__ = "730403386"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for elem in range(1, len(x)):
        current_val = x[elem]
        value = elem - 1
        while value >= 0 and current_val < x[value]:
            x[value + 1] = x[value]
            value -= 1
        x[value + 1] = current_val
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for value in range(len(x)):
        minimum = value
        for idx in range(value + 1, len(x)):
            if x[idx] < x[minimum]:
                minimum = idx
        if minimum != value:
            elem = x[value]
            x[value] = x[minimum]
            x[minimum] = elem
    return None
    