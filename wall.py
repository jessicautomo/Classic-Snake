from turtle import Turtle

class walls(Turtle):

    def __init__(self):
        super().__init__()
        self.coor = []
        self.width(7)
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.goto(-295,295)
        self.pendown()
        for i in range(4):
            for i in range(39):
                self.forward(15)
                self.get_coor()
            self.right(90)
        self.penup()
        self.goto(-230,250)
        self.pendown()
        self.right(90)
        for i in range(40):
            self.forward(10)
            self.get_coor()
        self.left(90)
        for i in range(10):
            self.forward(10)
            self.get_coor()
        self.penup()
        self.goto(-120,240)
        self.pendown()
        self.right(90)
        for i in range(20):
            self.forward(10)
            self.get_coor()
        self.penup()
        self.goto(-100,-50)
        self.pendown()
        self.left(90)
        for i in range(20):
            self.forward(15)
            self.get_coor()
        self.right(90)
        for i in range(10):
            self.forward(10)
            self.get_coor()
        self.penup()
        self.goto(0,250)
        self.pendown()
        for i in range(10):
            self.forward(10)
            self.get_coor()
        self.left(90)
        for i in range(20):
            self.forward(10)
            self.get_coor()
        self.right(90)
        for i in range(8):
            self.forward(15)
            self.get_coor()
        self.hideturtle()

    def get_coor(self):
        new = self.pos()
        self.coor.append(new)