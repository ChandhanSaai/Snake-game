from turtle import Turtle

INITIAL_POS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            turtle = Turtle()
            self.turtles.append(turtle)
            self.turtles[i].shape("square")
            self.turtles[i].color("white")
            self.turtles[i].penup()
            self.turtles[i].setpos(INITIAL_POS[i])

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def move_forward(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def move_backward(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def move_up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def move_down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def tail_adder(self):
        last_snake = self.turtles[len(self.turtles) - 1]
        pos_last_x = last_snake.xcor() - 20
        pos_last_y = last_snake.ycor()
        turtle = Turtle()
        self.turtles.append(turtle)
        self.turtles[len(self.turtles) - 1].shape("square")
        self.turtles[len(self.turtles) - 1].color("white")
        self.turtles[len(self.turtles) - 1].penup()
        self.turtles[len(self.turtles) - 1].goto(pos_last_x, pos_last_y)
