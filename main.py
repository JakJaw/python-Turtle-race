from turtle import Turtle, Screen
import random

is_on_race = False
screen = Screen()
screen.setup(500,400)
y_positions = [-90,-50,-10,30,70]
colors = ["red","blue","yellow","green","orange"]
all_turtles = []

bet = screen.textinput(title="Make ur bet (red/blue/yellow/green/orange): ", prompt="Which turtle will win the race? enter color: ")

for turtle in range(0,5):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)

if bet:
    is_on_race = True

while is_on_race:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on_race = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print("Congratulations, ur turtle won the race.")
                break
            else:
                print("Ur turtle lost the race.")
                break
        random_distance = random.randint(0,7)
        turtle.forward(random_distance)

screen.exitonclick()
