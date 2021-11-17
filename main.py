import random
from turtle import Turtle, Screen

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a Colour:")
colours = ["red", "blue", "green", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've Won!,{winning_colour} turtle is the winner")
            else:
                print(f"You've lost ,{winning_colour} turtle is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
