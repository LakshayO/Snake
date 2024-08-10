from Snake import Snake
from turtle import Screen
from Food import Food
from score import Score
import time

my = Screen()
my.tracer(0)
snake = Snake()
score = Score()
food = Food()

my.bgcolor("black")
my.title("Snake Game")
my.setup(height=600, width=600)

my.listen()

game_on = True
while game_on:
    time.sleep(0.1)
    my.update()
    snake.move()
    my.onkey(snake.Up, "Up")
    my.onkey(snake.Down, "Down")
    my.onkey(snake.Right, "Right")
    my.onkey(snake.Left, "Left")

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.point()
        snake.add_seg()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        snake.snake_reset()
        score.reset_score()
        snake = Snake()
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            score.reset_score()
            snake.snake_reset()
            snake = Snake()

my.exitonclick()
