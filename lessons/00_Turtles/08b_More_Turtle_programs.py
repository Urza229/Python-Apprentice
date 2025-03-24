"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

louis

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle
turtle.setup(width=600, height=600)
tina = turtle.Turtle()
tina.shape("triangle")
tina.speed(0)

tina.penup()

tina.right(90)
tina.forward(200)
tina.left(90)


forward = 5

tina.pendown()

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(3,100000000000000):
  left = 360 / sides
  make_shape(tina, forward, left, sides)

tina.penup()

tina.right(90)
tina.forward(75)


turtle.exitonclick()