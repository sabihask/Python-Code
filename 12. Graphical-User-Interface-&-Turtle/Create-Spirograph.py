import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge - Spirograph ########
# By trial and error found that the given angle and gap gives a proper spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        #turtle.heading returns the turtle’s current heading and setheading sets the orientation of the turtle to an angle
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


