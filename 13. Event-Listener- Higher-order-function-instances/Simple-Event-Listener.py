from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


# listen is used to listen to events on screen
screen.listen()
# onkey() method is used to collect key events
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
