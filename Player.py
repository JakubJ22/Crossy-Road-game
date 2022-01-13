from turtle import *

Y_AXE_DISTANCE = 30


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -282)
        self.undos = 0

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + Y_AXE_DISTANCE
        self.goto(x_cor, y_cor)
    
