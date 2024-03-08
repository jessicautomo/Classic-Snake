from turtle import Turtle
from food import Food
from snake import Snake


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write(f"Score: 0", align="center",font=("default",10,"normal"))
        self.hideturtle()

    def refresh(self,score):
        self.clear()
        self.write(f"Score: {score}", align="center",font=("default",10,"normal"))

    def game_over(self):
        self.color("#fff8e7")
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(f"GAME OVER", align="center",font=("default",30,"normal"))
        self.hideturtle()