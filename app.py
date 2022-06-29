from dragon import dragon, get_r
from turtle import Turtle, Screen

# Setup turtle
turtle = Turtle("turtle")
turtle.hideturtle()
turtle.speed(0)
turtle.color("#ff69aa")

# Setup Screen
screen = Screen()
screen.title("Dragon Curve")
screen.bgcolor("black")
screen.screensize(1920*3, 1080*3)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)


# Draw
LENGHT = 12
for element in dragon(15):
    if element == get_r():
        turtle.right(90)
        turtle.forward(LENGHT)
        # if you want circles use the line below instead
        # turtle.circle(-4, 90, 36)
    else:
        turtle.left(90)
        turtle.forward(LENGHT)
        # if you want circles use the line below instead
        # turtle.circle(4, 90, 36)

# When finished, click to exit
turtle.color("white")
turtle.write("click to exit", font=("Calibri", 16, "bold"))
screen.exitonclick()
