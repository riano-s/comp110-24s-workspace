"""EX08 - Ice cream cone on the beach scene."""

__author__ = "730403386"

from turtle import Turtle, colormode, done
colormode(255)

def main() -> None:
    """The entrypoint of my scene."""
    ice_cream_turtle: Turtle = Turtle()
    ice_cream_cone_turtle: Turtle = Turtle()
    sun_turtle: Turtle = Turtle()
    beach_turtle: Turtle = Turtle()
    draw_sun(sun_turtle, -190, 170, 60)
    draw_beach(beach_turtle, -400, 0)
    draw_ice_cream(ice_cream_turtle, 20, -190, 50, "pink")
    draw_ice_cream(ice_cream_turtle, 20, -120, 50, "light green")
    draw_ice_cream(ice_cream_turtle, 200, -190, 50, "purple")
    draw_ice_cream(ice_cream_turtle, 200, -120, 50, "orange")
    draw_ice_cream_cone(ice_cream_cone_turtle, -30, -160)
    draw_ice_cream_cone(ice_cream_cone_turtle, 150, -160)
    done()


def draw_ice_cream(turtle: Turtle, x: float, y: float, radius: float, color: str) -> None:
    """Draw ice cream scoops at a certain position and given radius & color."""
    # using new turtle function circle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_ice_cream_cone(turtle: Turtle, x: float, y: float) -> None:
    """Draw ice cream cone at a certain position."""
    # recursion
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    i: int = 0
    while i < 3:
        turtle.forward(100)
        turtle.right(120)
        i = i + 1
    turtle.end_fill()


def draw_sun(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw sun at a certain position and given radius."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_beach(turtle: Turtle, x: float, y: float) -> None:
    """Draw ocean and sand at a certain position."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(175)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(175)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-400, -175)
    turtle.pendown()
    turtle.color("tan")
    turtle.begin_fill()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(175)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(175)
    turtle.end_fill()
        

if __name__ == "__main__":
    main()