"""EX05 - Dictionary Functions."""

__author__ = "730403386"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary."""
    new_dict: dict[str, str] = dict()
    for key in input_dict:
        if input_dict[key] in new_dict:
            raise KeyError("Duplicated key!")
        new_dict[input_dict[key]] = key
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently in a dictionary."""
    color_count_dict: dict[str, int] = dict()
    fav_color: str = ""
    for key in input_dict:
        if (input_dict[key] in color_count_dict) is False:
            color_count_dict[input_dict[key]] = 1
        elif (input_dict[key] in color_count_dict):
            color_count_dict[input_dict[key]] += 1
    max: int = 0
    for key in color_count_dict:
        if color_count_dict[key] > max:
            max = color_count_dict[key]
            fav_color = key
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Creates dictionary where each value is the amount of times a key is found in a list."""
    count_dict: dict[str, int] = dict()
    for elem in input_list:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]: 
    """Sorts words alphabetically based on first letter in a dictionary."""
    sorted_dict: dict[str, list[str]] = dict()
    for elem in word_list:
        letter = elem[0].lower()
        if letter in sorted_dict:
            sorted_dict[letter].append(elem)
        else:
            sorted_dict[letter] = [elem]
    return sorted_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance dictionary with new attendance records."""
    if day in input_dict:
        input_dict[day].append(student)
    else:
        input_dict[day] = [student]