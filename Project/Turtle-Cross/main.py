import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
game_is_on = True
cars = CarManager()
screen.listen()
screen.onkey(player.move, "Up")
sb = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.gen_cars()
    cars.move_car()
    sb.reload_sb()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            sb.gameover()
        if player.ycor() > 300:
            player.start_pos()
            cars.level_move()
            sb.levelup()

screen.exitonclick()
