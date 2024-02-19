"""EX04 - List Utility Functions."""

__author__: "730403386"


def all(list: list[int], num: int) -> bool:
    """Returns bool depending on if all ints in list match the given int."""
    counter = 0
    while counter <= len(list) - 1:
        current_int = list[counter]
        if current_int == num:
            counter += 1
        else:
            return False
    return True
        

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    return


def extend(lista: list[int], listb: list[int]) -> None:
    "Appends list of integars to a list of integars."
    lista.append(listb)