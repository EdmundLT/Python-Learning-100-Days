import turtle
from turtle import Turtle, Screen
import random

color_list = [
    (235, 234, 231), (234, 229, 231), (236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93),
    (231, 238, 234), (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0),
    (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)
]
turtle.colormode(255)

timmy = Turtle()
timmy.pu()
timmy.setposition(-200, -200)
timmy.hideturtle()

def go_right():
    for x in range(10):
        color = random.choice(color_list)
        timmy.setheading(0)
        timmy.pd()
        timmy.dot(20, color)
        timmy.pu()
        timmy.fd(50)

def go_left():
    for x in range(10):
        color = random.choice(color_list)
        timmy.setheading(180)
        timmy.dot(20, color)
        timmy.fd(50)
        

def go_up():
    timmy.bk(50)
    timmy.seth(90)
    timmy.fd(50)


Screen()
for x in range(5):
    go_right()
    go_up()
    go_left()
    go_up()
    
Screen().exitonclick()
