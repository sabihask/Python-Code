import turtle as t
#Turtle is a special feathers of Python. Using Turtle, we can easily draw in a drawing board.
#First we import the turtle module. Then create a window, next we create turtle object and using turtle method we can draw in the drawing board.

# create an instance of the class Turtle
tim = t.Turtle()

########### Challenge - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
