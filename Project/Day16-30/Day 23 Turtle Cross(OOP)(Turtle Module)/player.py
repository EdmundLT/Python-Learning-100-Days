from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.setheading(90)
        self.start_pos()

    def start_pos(self):
        self.setpos(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)
