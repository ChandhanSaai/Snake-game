from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.restart()

    def restart(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)
