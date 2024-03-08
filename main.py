import time
from turtle import Screen
from scoreboard import ScoreBoard

from snake import Snake
from food import Food

screen = Screen()
snk = Snake()
food = Food()
score = ScoreBoard()

screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.listen()
screen.onkey(snk.up, "Up")
screen.onkey(snk.down, "Down")
screen.onkey(snk.left, "Left")
screen.onkey(snk.right, "Right")
snk.make_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snk.move_snake()
    if snk.head.distance(food) < 15:
        food.refresh()
        snk.extend_snake()
        score.increase_score()
    if snk.head.xcor() > 300 or snk.head.xcor() < -300 or snk.head.ycor() > 300 or snk.head.ycor() < -300:
        score.reset_game()
        snk.reset_snake()

    for seg in snk.segments[1:]:
        if snk.head.distance(seg) < 10:
            score.reset_game()
            snk.reset_snake()

screen.exitonclick()
