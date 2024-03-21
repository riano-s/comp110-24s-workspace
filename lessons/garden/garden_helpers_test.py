"""Test my garden functions."""

__author__ = "730403386"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_new_kind() -> None:
    """New kind of plant and plant name should be added to garden dictionary."""
    garden_dict = {"flower": ["tulip"]}
    new_kind = "flower"
    new_plant_type = "rose"
    add_by_kind(garden_dict, new_kind, new_plant_type)
    assert garden_dict == {"flower": ["tulip", "rose"]}


def test_add_known_kind() -> None:
    """A kind of plant and plant name already seen in the dictionary should not be added."""
    garden_dict = {"flower": ["tulip", "sunflower"]}
    new_kind = "flower"
    new_plant_type = "sunflower"
    add_by_kind(garden_dict, new_kind, new_plant_type)
    assert garden_dict == {"flower": ["tulip", "sunflower", "sunflower"]}


def test_add_new_date() -> None:
    """New month and plant name should be added to garden dictionary."""
    garden_dates = {"April": ["tulip"]}
    month = "May"
    plant_type = "sunflower"
    add_by_date(garden_dates, month, plant_type)
    assert garden_dates == {"April": ["tulip"], "May": ["sunflower"]}


def test_add_no_plant() -> None:
    """Should return a dictionary with the date but an empty list."""
    garden_dates = {"April": ["rose"]}
    month = "July"
    plant_type = ""
    add_by_date(garden_dates, month, plant_type)
    assert garden_dates == {"April": ["rose"], "July": [""]}


def test_lookup_kind_and_date() -> None:
    """Should return list of plants to plant during a specific month."""
    kind: str = "flower"
    month: str = "May"
    kind_of_plants: dict[str, list[str]] = {kind: ["tulip", "rose", "sunflower"]}
    dates_to_plant: dict[str, list[str]] = {month: ["tulip"], "March": ["rose", "carnation"]}
    assert lookup_by_kind_and_date(kind_of_plants, dates_to_plant, kind, month) == "flowers to plant in May: ['tulip']"


def test_lookup_kind_and_empty_date() -> None:
    """Should return a list of plants to plant during a month not found in the dates dictionary."""
    kind: str = ""
    month: str = "June"
    kind_of_plants: dict[str, list[str]] = {kind: ["rose", "sunflower"]}
    dates_to_plant: dict[str, list[str]] = {month: ["rose", "zinnia"], "May": ["sunflower"]}
    assert lookup_by_kind_and_date(kind_of_plants, dates_to_plant, kind, month) == "s to plant in June: ['rose']"