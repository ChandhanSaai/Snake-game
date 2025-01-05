from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pendown()
        self.shapesize(stretch_wid=0.0001, stretch_len=0.0001)
        self.setpos(0, 350)
        self.pencolor("white")
        self.score_counter()

    def score_counter(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 20, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(x=0.0, y=0.0)
        self.write("Game Over",  False, "center", font=("Arial", 20, "normal"))
