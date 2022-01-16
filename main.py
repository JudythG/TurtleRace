import turtle
from turtle import Turtle, Screen
import random

TURTLE_SPACING = 40
STARTING_LINE = -230
FINISH_LINE = 220


def get_bet():
    bet = ""
    while bet not in colors:
        bet = screen.textinput(title="Make Your Bet",
                               prompt=f"Which turtle will win the race? Enter a color ({', '.join(colors)}): ")
    return bet


def init_turtles():
    """ create one turtle for each color; set turtles at the starting line """
    y_start = TURTLE_SPACING * -len(colors) / 2
    x_start = STARTING_LINE
    turtle_list = []
    for color in colors:
        t = Turtle("turtle")
        t.color(color)
        t.penup()
        t.goto(x=x_start, y=y_start)
        turtle_list.append(t)
        y_start += 40
    return turtle_list


def move_turtle(t):
    """ Move turtle forward by a random amount """
    t.forward(random.randint(0, 10))


def race_turtles():
    """ Move each turtle forward by a random amount until one crosses the finish line """
    race_won = False
    while not race_won:
        for t in turtles:
            move_turtle(t)
            if t.xcor() >= FINISH_LINE:
                race_won = True
                return t.pencolor()


def output_results(bet, winning_color):
    if user_bet == winner:
        print(f"You won. The {winner} turtle is the winning turtle.")
    else:
        print(f"You lost. The {winner} turtle is the winning turtle.")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

user_bet = get_bet()
turtles = init_turtles()
winner = race_turtles()

screen.exitonclick()

output_results(bet=user_bet, winning_color=winner)
