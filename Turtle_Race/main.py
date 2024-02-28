import random
import turtle
from turtle import Screen, Turtle
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make a bet", "Which turtle do you think will win??: ")
colors = ["red","blue","green","yellow","purple","orange"]
y_pos = [-70,-40,-10,20,50,80]
all_t = []
for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-230, y_pos[turtle_index])
    all_t.append(tim)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_t:
        if turtle.xcor() > 230:
            print(f"Winner is {turtle.pencolor()}")
            is_race_on = False
        move = random.randint(1, 10)
        turtle.forward(move)


screen.exitonclick()