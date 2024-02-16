"""Mutating functions."""

__author__ = "730403386"


def manual_append(numbers: list[int], num: int) -> None:
    """Appends integar to list of integars."""
    numbers.append(num)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(list: list[int]) -> None:
    """Doubles every element in the list."""
    counter = 0
    while counter <= len(list) - 1:
        current_number = list[counter]
        list[counter] = current_number * 2
        counter += 1
        
    
b: list[int] = [3, 7, 9, 11]
double(b)
print(b)