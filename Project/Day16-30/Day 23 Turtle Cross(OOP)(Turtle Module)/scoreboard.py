from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 250)

    def reload_sb(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def levelup(self):
        self.clear()
        self.level += 1
        self.reload_sb()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
