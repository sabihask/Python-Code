import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fwd():
    tim.forward(50)


def move_bkwd():
    tim.backward(50)


def move_clockwise():
    tim.left(10)


def move_anti_clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()

# event listener
screen.listen()
screen.onkey(key="W", fun=move_fwd)
screen.onkey(key="S", fun=move_bkwd)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="A", fun=move_anti_clockwise)
screen.onkey(key="C", fun=clear_drawing)
screen.exitonclick()
