from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# triangle
leo.penup()
leo.goto(55, 70)
leo.pendown()
leo.color(255, 51, 135)

leo.begin_fill()
leo.speed(50)
i: int = 0
while (i < 3):
    leo.forward(400)
    leo.left(220)
    i = i + 1
leo.end_fill()
leo.hideturtle()


bob: Turtle = Turtle()

bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.color(0, 0, 0)

bob.begin_fill()
bob.speed(80)
a: int = 0
while (a < 3): 
    bob.forward(300)
    bob.left(120)
    i = i + 1
bob.end_fill()
bob.hideturtle()
done()
