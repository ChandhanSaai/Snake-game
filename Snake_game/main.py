import time
from turtle import Screen
import snake
import food
import scoreboard

display = Screen()

display.screensize(600, 600)
display.bgcolor("black")
display.title("snake game")
display.tracer(0)
snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

display.listen()
display.onkey(snake.move_forward, "Right")
display.onkey(snake.move_up, "Up")
display.onkey(snake.move_down, "Down")
display.onkey(snake.move_backward, "Left")


game_running = True
while game_running:
    display.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.restart()
        score.score_counter()
        snake.tail_adder()

    if snake.turtles[0].xcor() > 400 or snake.turtles[0].xcor() < -400 or snake.turtles[0].ycor() < -400 or snake.turtles[0].ycor() > 400:
        game_running = False
        score.game_over()

    for turtles in snake.turtles[1:]:
        if snake.turtles[0].distance(turtles) < 10:
            game_running = False
            score.game_over()

display.exitonclick()
