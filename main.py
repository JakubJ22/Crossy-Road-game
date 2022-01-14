from turtle import *
from Player import Player
from Score_board import Score_Board
from Cars import Cars
import time


def game_on():
    """All game is one function, because we will use recursion (22 line) to start new game"""
    game_is_on = True
    delay = 0.02
    """Setting up the screen settings"""
    screen = Screen()
    screen.setup(600, 600)
    screen.title("Cross the street")
    screen.bgcolor("black")
    screen.tracer(0)

    def next_round():
        """It is bound to spacebar, we can start new game"""
        screen.reset()
        game_on()

    """Creating game objects"""
    player = Player()
    board = Score_Board()
    cars = [Cars() for _ in range(45)]

    """Binding keys"""
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_up, "w")

    screen.listen()
    """Infinite loop below turns our game in motion """
    while game_is_on:
        "slowing down our game"
        time.sleep(delay)

        """Lv up (more 'cars' and increased speed)"""
        if player.ycor() > 290:
            player.goto(0, -282)
            board.score += 1
            board.give_score()
            for _ in range(15):
                cars.append(Cars())
            for car in cars:
                car.x_axe_move += 1.5
        else:
            for car in cars:
                car.move()
                """Detecting colission with obstacles"""
                if car.distance(player) < 25:
                    for car in cars:
                        """Hiding obstacles to show message"""
                        if car.ycor() < 60 and car.ycor() > -50:
                            car.hideturtle()
                    board.game_over()
                    game_is_on = False

                    """Binding 'choice' keys"""
                    screen.onkey(screen.bye, "Escape")
                    screen.onkey(next_round, "space")

        screen.update()
    screen.exitonclick()


game_on()
