import random
from turtle import Turtle


class Paddle(Turtle):
    MOVE_DISTANCE = 4

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=0.5)
        self.penup()
        self.goto(position)
        self.starting_position = position

    def go_up(self):
        self.move_by(20)

    def go_down(self):
        self.move_by(-20)

    def move_by(self, distance):
        new_y = self.ycor() + distance

        if new_y > 250:
            new_y = 250
        elif new_y < -250:
            new_y = -250

        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(self.starting_position)
