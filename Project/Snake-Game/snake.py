from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(pos)
        self.segs.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segs) - 1, 0, -1):
            new_x = self.segs[seg_num - 1].xcor()
            new_y = self.segs[seg_num - 1].ycor()
            self.segs[seg_num].goto(new_x, new_y)

        self.head.fd(MOVE_DIS)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        self.add_segment(self.segs[-1].position())
