from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
l_pad = Paddle((-350, 0))
r_pad = Paddle((350, 0))

screen.listen()
screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")

screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")

game_is_on = True
speed = 0.05
while game_is_on:
    time.sleep(speed)
    screen.update()
    scoreboard.update_scorebaord()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_pt()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_pt()
        ball.reset()

    else:
        ball.move()
screen.exitonclick()
