"""Splitting a dictionary into two lists."""

__author__ = "730403386"


def get_keys(dict: dict[str, int]) -> list[str]:
    """Returns the keys in a dictionary as a list."""
    key_list: list[str] = list()
    for key in dict:
        key_list.append(key)
    return key_list


def get_values(dict: dict[str, int]) -> list[int]:
    """Returns the values in a dictionary as a list."""
    value_list: list[int] = list()
    for key in dict:
        value_list.append(dict[key])
    return value_list