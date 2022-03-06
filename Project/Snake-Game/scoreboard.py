from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.userscore = 0
        self.pu()
        self.ht()

    def show_scoreboard(self):

        self.goto(0, 270)
        self.color("white")
        self.write(f"Score : {self.userscore}", False,
                   align=ALIGNMENT, font=FONT)

    def scored(self):
        self.clear()
        self.userscore += 1
        self.show_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAMEOVER!", False,
                   align=ALIGNMENT, font=FONT)
