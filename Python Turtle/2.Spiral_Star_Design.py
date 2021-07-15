# Spiral Star Design

import turtle
col = ('red','yellow','green','cyan','violet','white','indigo')
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor('black')
t.speed(0)

col = ('purple','green','red','cyan')

for i in range(180):
    t.pencolor(col[i%4])
    t.forward(i*4)
    t.right(155)