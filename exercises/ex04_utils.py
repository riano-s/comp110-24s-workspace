"""EX04 - List Utility Functions."""

__author__ = "730403386"


def all(list: list[int], num: int) -> bool:
    """Returns bool depending on if all ints in list match the given int."""
    counter = 0
    if list == []:
        return False
    while counter <= len(list) - 1:
        current_int = list[counter]
        if current_int == num:
            counter += 1
        else:
            return False
    return True
        

def max(input: list[int]) -> int:
    """Returns the highest number in a list of integars."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    counter = 1
    index = 0
    max = input[index]
    while counter <= len(input) - 1:
        if input[counter] > max:
            max = input[counter]
        counter += 1
    return max

    
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns bool depending on whether all elements in two separate lists are equal."""
    counter = 0
    if len(list1) != len(list2):
        return False
    while counter <= len(list1) - 1 and len(list2) - 1:
        if list1[counter] == list2[counter]:
            counter += 1
        else:
            return False
    return True


def extend(lista: list[int], listb: list[int]) -> None:
    """Appends list of integars to a list of integars."""
    counter = 0
    while counter <= len(listb) - 1:
        lista.append(listb[counter])
        counter += 1

        