from dragon import dragon, R
from turtle import Turtle, Screen

# Turtle setup
turtle = Turtle("turtle")
turtle.hideturtle()
turtle.speed("fastest")
turtle.color("#ff69aa")

# Screen setup
screen = Screen()
screen.title("Dragon Curve")
screen.bgcolor("black")
screen.screensize(1920*3, 1080*3)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)


# Draw
LENGTH = 10
turtle.forward(LENGTH)
for element in dragon():
    if element == R:
        turtle.right(90)
        turtle.forward(LENGTH)
        # if you want circles use the line below instead
        # turtle.circle(-4, 90, 36)
    else:
        turtle.left(90)
        turtle.forward(LENGTH)
        # if you want circles use the line below instead
        # turtle.circle(4, 90, 36)

# When finished, click to exit
turtle.color("white")
turtle.write("click to exit", font=("Calibri", 16, "bold"))
screen.exitonclick()
