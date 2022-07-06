from dragon import dragon, R
from turtle import Turtle, Screen

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--delay",
        type=int,
        default=1,
        help="Drawing delay in ms (Use `0` for very fast drawings)",
    )
    parser.add_argument(
        "--line-length", type=int, default=10, help="Length of the lines."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    # Turtle setup
    turtle = Turtle("turtle")
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.color("#ff69aa")

    # Screen setup
    screen = Screen()
    screen.title("Dragon Curve")
    screen.bgcolor("black")
    screen.delay(args.delay)
    screen.screensize(1920 * 3, 1080 * 3)
    screen.setup(width=1.0, height=1.0, startx=None, starty=None)

    # Draw
    turtle.forward(args.line_length)
    for element in dragon():
        if element == R:
            turtle.right(90)
            turtle.forward(args.line_length)
            # if you want circles use the line below instead
            # turtle.circle(-4, 90, 36)
        else:
            turtle.left(90)
            turtle.forward(args.line_length)
            # if you want circles use the line below instead
            # turtle.circle(4, 90, 36)


if __name__ == "__main__":
    main()
