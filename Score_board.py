from turtle import *
FONT = ('Arial', 15, 'normal')


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.position = position
        self.score = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.give_score()

    def give_score(self):
        """Refreshing the score """
        self.clear()
        self.write(f"Level {self.score}", align="center",
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"Game over", align="center",
                   font=('Arial', 30, 'normal'))
        self.what_next()

    def what_next(self):
        self.goto(0, -25)
        self.write(f"Press Esc to exit or Spacebar to play again", align="center",
                   font=('Arial', 15, 'normal'))
