"""EX06 - Testing Dictionary Functions."""

__author__ = "730403386"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_key_error_use() -> None:
    """Tests the use of the Key Error in the function."""
    with pytest.raises(KeyError):
        my_dictionary = {'name': 'james', 'lastname': 'james'}
        assert invert(my_dictionary) == KeyError


def test_invert_use() -> None: 
    """Tests if keys and values in a dictionary are inverted."""
    pets_dictionary = {'dog': 'buddy', 'cat': 'tori'}
    assert invert(pets_dictionary) == {'buddy': 'dog', 'tori': 'cat'}


def test_inverts_empty_value() -> None:
    """Tests if key and empty value will invert."""
    pets_dictionary = {'dog': '', 'cat': 'tori'}
    assert invert(pets_dictionary) == {'': 'dog', 'tori': 'cat'}


def test_favorite_color_use() -> None:
    """Tests if most frequent color in a dictionary is returned."""
    colors_dictionary = {'Brad': 'blue', 'Carmen': 'pink', 'Jude': 'pink'}
    assert favorite_color(colors_dictionary) == 'pink'


def test_favorite_color_from_one_value() -> None:
    """Tests if most frequent color in a dictionary is returned when it is the only color given."""
    colors_dictionary = {'banana': 'yellow'}
    assert favorite_color(colors_dictionary) == 'yellow'


def test_no_color() -> None:
    """Tests if a color is returned when no color is inputted."""
    colors = {'banana': '', 'pineapple': '', 'apple': 'red'}
    assert favorite_color(colors) == ''


def test_count_use() -> None:
    """Tests if dictionary values are the number of times a key is found in a list."""
    animal_input = ['panda', 'alligator', 'panda', 'giraffe', 'panda']
    assert count(animal_input) == {'panda': 3, 'alligator': 1, 'giraffe': 1}


def test_count_for_one_key() -> None:
    """Tests if dictionary value is returned based on the number of times a key is inputted."""
    fruit_input = ['pear', 'pear', 'pear', 'pear', 'pear', 'pear', 'pear', 'pear']
    assert count(fruit_input) == {'pear': 8}


def test_count_on_empty_list() -> None:
    """Tests if dictionary value is return for empty list."""
    fruit_input = ['', '', '']
    assert count(fruit_input) == {'': 3}


def test_alphabetizer_use() -> None:
    """Tests if words are sorted alphabetically."""
    dog_breeds = ['pitbull', 'husky', 'schnauzer', 'poodle', 'hound']
    assert alphabetizer(dog_breeds) == {'p': ['pitbull', 'poodle'], 'h': ['husky', 'hound'], 's': ['schnauzer']}


def test_alphabetizer_for_one_word() -> None:
    """Tests if one word can be sorted alphabetically."""
    dog_breeds = ['pitbull']
    assert alphabetizer(dog_breeds) == {'p': ['pitbull']}


def test_alphabetizer_on_same_words() -> None:
    """Tests if a list of the same word can be alphabetized."""
    dog_breeds = ['poodle', 'poodle', 'poodle']
    assert alphabetizer(dog_breeds) == {'p': ['poodle', 'poodle', 'poodle']}


def test_update_attendance_use() -> None:
    """Tests if attendance dictionary is updated with new record of a previously recorded day."""
    attendance = {'Monday': ['Chloe', 'Henry'], 'Wednesday': ['Henry'], 'Friday': ['Chloe']}
    day = 'Friday'
    student = 'Harry'
    update_attendance(attendance, day, student)
    assert attendance == {'Monday': ['Chloe', 'Henry'], 'Wednesday': ['Henry'], 'Friday': ['Chloe', 'Harry']}


def test_update_attendance_new_day() -> None:
    """Tests if attendance dictionary is updated with new record of a new day."""
    attendance = {'Monday': ['Chloe', 'Henry'], 'Wednesday': ['Henry']}
    day = 'Tuesday'
    student = 'Harry'
    update_attendance(attendance, day, student)
    assert attendance == {'Monday': ['Chloe', 'Henry'], 'Wednesday': ['Henry'], 'Tuesday': ['Harry']}


def test_update_attendance_no_student() -> None:
    """Tests if attendance dictionary is updated with new record with an empty name string."""
    attendance = {'Monday': ['Chloe', 'Henry'], 'Friday': ['Chloe']}
    day = 'Wednesday'
    student = ''
    update_attendance(attendance, day, student)
    assert attendance == {'Monday': ['Chloe', 'Henry'], 'Friday': ['Chloe'], 'Wednesday': ['']}