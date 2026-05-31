import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(800, 600)

# score
score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-380, 260)

def show_score():
    pen.clear()
    pen.write("Score: " + str(score), font=("Arial", 16, "bold"))

show_score()

# fish list
fishes = []

colors = ["orange", "yellow", "red", "green"]

for i in range(5):
    f = turtle.Turtle()
    f.shape("turtle")
    f.color(random.choice(colors))
    f.penup()
    f.goto(random.randint(-300, 300), random.randint(-200, 200))
    fishes.append(f)

# food
food = turtle.Turtle()
food.shape("circle")
food.color("brown")
food.penup()
food.goto(0, 0)

def feed(x, y):
    global score
    food.goto(random.randint(-300, 300), random.randint(-200, 200))
    score += 1
    show_score()

food.onclick(feed)

# simple movement (NO timer, NO class)
while True:
    for f in fishes:
        f.forward(2)

        if f.xcor() > 400:
            f.goto(-400, random.randint(-200, 200))