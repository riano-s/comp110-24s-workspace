"""Define Point class."""

from __future__ import annotations

__author__ = "730403386"


class Point:
    """Class that has (x,y) coordinates."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Constructor for Point class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates each attribute so that it updates to the attribute * the factor."""
        self.x *= factor
        self.y *= factor
        
    def scale(self, factor: int) -> Point:
        """Returns new Point in which each attribute has been multiplied by the factor."""
        point_x = self.x * factor
        point_y = self.y * factor
        return Point(point_x, point_y)