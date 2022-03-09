from turtle import Turtle, Screen
import random
from xml.etree.ElementPath import get_parent_map
from data import colours
import turtle

my_screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.speed("fastest")

turtle.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


def random_drawing():
    heading = 0
    for x in range(100):
        timmy.pencolor(random_color())
        timmy.circle(100)
        heading += 5
        timmy.setheading(heading)


random_drawing()
my_screen.exitonclick()
