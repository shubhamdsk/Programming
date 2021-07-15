# Spiral Design

import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor('black')

t.speed(100)
screen.setup(700,700)

col = ('green','cyan','purple','red')

for c in range(300):
    t.pencolor(col[c%4])
    t.width(2)
    t.forward(c)
    t.right(89)
    t.forward(c*2)
    t.right(89)