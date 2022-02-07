from turtle import Turtle, Screen
import random

new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "yellow", "green", "blue", "pink", "purple"]
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color.\nChoose color - red, yellow, green, blue, pink, purple")
y_position=[-70, -40, -10, 20, 40, 60]
game_on=False
turtle_list=[]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)


if user_bet:
     game_on=True


while game_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            game_on = False
            winning_turtle=turtle.pencolor()
            if winning_turtle == user_bet:
                print("You won!!")

            else:
                print(f"You loose.Winning turtle is {winning_turtle}")
            print()
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
