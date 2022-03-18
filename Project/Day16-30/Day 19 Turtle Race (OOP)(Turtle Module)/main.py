from turtle import Turtle, Screen
import random

colors = ["red", "blue", "black", "grey", "brown", "yellow"]
turtle_list = []
is_race_on = False


def turtle_race():
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    color = 0
    y = -80
    for turtle in range(6):
        new_turtle = Turtle()
        new_turtle.color(colors[color])
        new_turtle.shape("turtle")
        new_turtle.pu()
        new_turtle.goto(-200, y)
        color += 1
        y += 40
        turtle_list.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You are win. The {winning_color} turtle won.")
                    is_race_on = False
                else:
                    print(f"You are lose. The {winning_color} turtle won.")
                    is_race_on = False
            ran_distance = random.randint(0, 10)
            turtle.fd(ran_distance)


screen = Screen()
screen.setup(500, 400)
turtle_race()

screen.exitonclick()
