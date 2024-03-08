from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import walls
import time

screen = Screen()
screen.tracer(0,0)

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

walls = walls()

snake = Snake()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

scoreboard = Scoreboard()
score = 0
food = Food()

game_on = True
while game_on:
    #screen update every 0.1 seconds, snake.move() function every 0.1 seconds
        ##how it works: wait 0.1 seconds, then move again
    time.sleep(0.1)
    screen.update()
    snake.move()

    for coordinate in walls.coor:
        if snake.head.distance(coordinate) <= 14:
            game_on = False
            scoreboard.game_over()
            time.sleep(0.1)
            screen.update()
        while food.distance(coordinate) < 20:
            food.hideturtle()
            food.refresh()
            food.showturtle()

    if snake.head.distance(food) < 15:
        #screen.tracer(0,0)
        food.refresh()
        snake.extend()
        score += 1
        scoreboard.refresh(score)

    #detect tail collision
    #segments[1:] meaning segment 1 until last segment(everything
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()



