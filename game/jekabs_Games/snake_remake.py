# Imports
import os
import turtle

# Variables
global starting
starting = 0
menu = turtle.Turtle()
# Set up the screen as fullscreen
bkground = turtle.Screen()
bkground.title("Jekabs Snake Game")
bkground.bgcolor("black")
bkground.setup(width=1920, height=1080)
bkground.tracer(0)  # Turns off the screen updates


# Game Menu
def get_high_score():
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as f:
            high_score = f.read().split("\n")
            if high_score:
                # set all the high socre as intiger and get the highest number
                highest_score = max(int(i) for i in high_score)
                return highest_score
            else:
                return "None"


def starting_menu():
    pressed = 1
    while pressed == 1:
        print(pressed)
        menu.speed(0)
        menu.shape("circle")
        menu.color("white")
        menu.penup()
        menu.hideturtle()
        menu.goto(0, 0)
        menu.write(
            "Thank you for using Jekabs Snake Game Press Enter to start \n Controls: W - Up, A - Left, S - Down, D - Right \n High Score: " + str(
                get_high_score()) + " \n Can you beat it?? \n Press Space to start the game", align="center",
            font=("Courier", 24, "normal"))
        bkground.update()
        bkground.listen()  # when user presses space end the while loop
        bkground.onkeypress(start_game, "space")



def start_game():
    #when pressed stop the while loop from starting menu and show a snake
    pressed = 0
    print(pressed)
    menu.clear()
    menu.goto(0, 0)
    menu.write("Game Started", align="center", font=("Courier", 24, "normal"))
    bkground.update()
    bkground.listen()
    bkground.onkeypress(starting_menu, "space")
    bkground.onkeypress(starting_menu, "w")
    bkground.onkeypress(starting_menu, "a")
    bkground.onkeypress(starting_menu, "s")
    bkground.onkeypress(starting_menu, "d")
    bkground.onkeypress(starting_menu, "Return")
    bkground.onkeypress(starting_menu, "Up")
    bkground.onkeypress(starting_menu, "Down")
    bkground.onkeypress(starting_menu, "Left")
    bkground.onkeypress(starting_menu, "Right")


starting_menu()
