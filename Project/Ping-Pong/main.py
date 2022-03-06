# Day 22 Project - PING PONG

- main.py
    
    ```python
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
    ```
    
- scoreboard.py
    
    ```python
    from turtle import Turtle
    FONT = ('Arial', 80, 'normal')
    
    class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.l_userscore = 0
            self.r_userscore = 0
            self.color("white")
            self.pu()
            self.hideturtle()
    
        def update_scorebaord(self):
            self.goto(-100, 200)
            self.write(self.l_userscore, align="center", font=FONT)
            self.goto(100, 200)
            self.write(self.r_userscore, align="center", font=FONT)
    
        def l_pt(self):
            self.clear()
            self.l_userscore += 1
    
        def r_pt(self):
            self.clear()
            self.r_userscore += 1
    ```
    
- paddle.py
    
    ```python
    from turtle import Turtle
    
    class Paddle(Turtle):
        def __init__(self, position):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.shapesize(5, 1)
            self.pu()
            self.goto(position)
    
        def move_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    
        def move_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
    ```
    
- ball.py
    
    ```python
    from turtle import Turtle
    
    class Ball(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.color("white")
            self.pu()
            self.x_move = 10
            self.y_move = 10
    
        def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
    
        def reset(self):
            self.home()
            self.x_move *= -1
            self.y_move *= -1
    
        def bounce_y(self):
            self.y_move *= -1
    
        def bounce_x(self):
            self.x_move *= -1
    ```
    
-
