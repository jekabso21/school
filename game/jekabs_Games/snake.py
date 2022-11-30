import random
import time
import turtle

delay = 0.2

# Score
score = 0
high_score = 0

#for special effects config
effets = True

# Set up the screen
bkground = turtle.Screen()
bkground.title("Snake Game by @jekabs")
bkground.bgcolor("black")
bkground.setup(width=600, height=600)
bkground.tracer(0)  # Turns off the screen updates

# Snake shead
shead = turtle.Turtle()
shead.speed(0)
shead.shape("circle")
shead.color("white")
shead.penup()
shead.goto(0, 0)
shead.direction = "stop"

# Snake food
sfood = turtle.Turtle()
sfood.speed(0)
sfood.shape("circle")
sfood.color("red")
sfood.penup()
sfood.goto(0, 100)

segments = []

# Pen
text = turtle.Turtle()
text.speed(0)
text.shape("circle")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
def go_up():
    if shead.direction != "dobkground":
        shead.direction = "up"


def go_dobkground():
    if shead.direction != "up":
        shead.direction = "dobkground"


def go_left():
    if shead.direction != "right":
        shead.direction = "left"


def go_right():
    if shead.direction != "left":
        shead.direction = "right"



def move():
    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 20)

    if shead.direction == "dobkground":
        y = shead.ycor()
        shead.sety(y - 20)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x - 20)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x + 20)


# Keyboard bindings
bkground.listen()
bkground.onkeypress(go_up, "w")
bkground.onkeypress(go_dobkground, "s")
bkground.onkeypress(go_left, "a")
bkground.onkeypress(go_right, "d")

# Main game loop
while True:
    bkground.update()

    # Check for a collision with the border
    if shead.xcor() > 290 or shead.xcor() < -290 or shead.ycor() > 290 or shead.ycor() < -290:
        time.sleep(1)
        shead.goto(0, 0)
        shead.direction = "stop"

        # Hide the graphics
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the graphics list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if shead.distance(sfood) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        sfood.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        if effets == True:
            rnd = random.randint(0, 10)
            if rnd > 8:
                color = random.choice(['green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black'])
                bkground.bgcolor('green')
                time.sleep(0.1)
                bkground.bgcolor('purple')
                time.sleep(0.1)
                bkground.bgcolor('pink')
                time.sleep(0.1)
                bkground.bgcolor('white')
                time.sleep(0.1)
                bkground.bgcolor(color)
            rand = random.randint(0, 10)
            print(rand)
            if rand > 5:
                print('special effect')
                print(sppedup)




        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the shead is
    if len(segments) > 0:
        x = shead.xcor()
        y = shead.ycor()
        segments[0].goto(x, y)

    move()

    # Check for shead collision with the body segments
    for segment in segments:
        if segment.distance(shead) < 20:
            time.sleep(1)
            shead.goto(0, 0)
            shead.direction = "stop"

            # Hide the segments

            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            text.clear()
            text.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

bkground.mainloop()
