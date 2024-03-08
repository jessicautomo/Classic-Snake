from turtle import Turtle, Screen
import time

START_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
screen = Screen()

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.hideturtle()
        snake.goto(position)
        self.segments.append(snake)
        snake.showturtle()


    #mechanism for extend
        ##add segment to position of -1(tail of snake)
    def extend(self):
        self.add_segment(self.segments[-1].position())


    #mechanism for move function
        ##starting from the tail of the snake, move each square segment to the position of the segment adjacent to it in the self.segments([])
        ##the for loop ends at the penultimate segment(does not include the segment at the 0th position, alas the head of the snake)
        ##the head is simply moved forward by MOVE_DISTANCE
        ##so basically we simply make the head move forward and all the other segments just take the place of the segment in front of it
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            print(segment)
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)






