"""EX05 - Dictionary Functions."""

__author__ = "730403386"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary."""
    counter: dict[str, str] = dict()
    new_dict: dict[str, str] = dict()
    for key in input_dict:
        temp_1 = key
        temp_2 = input_dict[key]
        new_dict[temp_2] = temp_1
    return new_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]: 
    """Sorts words alphabetically based on first letter in a dictionary."""
    counter_dict: dict[str, str] = dict()
    
                

print(alphabetizer(["cat", "apple", "zoo","Turtle","Crocodile"]))


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance dictionary with new attendance records."""
    if day in input_dict:
        input_dict[day].append(student)
    else:
        input_dict[day] = student




    

        





