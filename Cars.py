from turtle import *
import random

COLORS = ["red", "yellow", "blue", "orange", "purple", "green"]


class Cars(Turtle):
    def __init__(self):
        super().__init__("square")
        self.X_AXE = random.randrange(-250, 1000, 50)
        self.Y_AXE = random.randrange(-250, 280, 60)
        self.penup()
        self.speed("slowest")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(self.X_AXE, self.Y_AXE)
        self.resizemode("user")
        self.shapesize(1, 2)
        self.x_axe_move = 4

    def move(self):
        if self.xcor() < -310:
            self.goto(self.X_AXE+random.randint(600, 800), self.Y_AXE)
        else:
            self.forward(self.x_axe_move)
