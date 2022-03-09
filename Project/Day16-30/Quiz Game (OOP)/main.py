from turtle import Turtle, Screen

my_screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

writing = True
while writing:
    line_number = 3
    angle = 360 / line_number
    for x in range(line_number):
        timmy.fd(100)
        timmy.right(angle)
    line_number += 1

my_screen.exitonclick()
