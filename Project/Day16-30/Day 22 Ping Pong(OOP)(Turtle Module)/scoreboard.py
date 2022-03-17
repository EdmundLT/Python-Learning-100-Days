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
