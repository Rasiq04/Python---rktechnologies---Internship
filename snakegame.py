import turtle
import time
import random

delay = 0.1

# Score
score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Up"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Snake body
segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 270)
score_display.write("Score: 0", align="left", font=("Courier", 16, "normal"))


# Functions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"


def go_down():
    if head.direction != "Up":
        head.direction = "Down"


def go_left():
    if head.direction != "Right":
        head.direction = "Left"


def go_right():
    if head.direction != "Left":
        head.direction = "Right"


def move():
    if head.direction == "Up":
        head.sety(head.ycor() + 20)
    elif head.direction == "Down":
        head.sety(head.ycor() - 20)
    elif head.direction == "Left":
        head.setx(head.xcor() - 20)
    elif head.direction == "Right":
        head.setx(head.xcor() + 20)


# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Up"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random location
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")  # You can customize the snake color
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        score_display.clear()
        score_display.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Up"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))

    time.sleep(delay)

wn.mainloop()
