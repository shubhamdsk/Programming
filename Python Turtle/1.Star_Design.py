# Star Design

import turtle
turtle.bgcolor("black")

turtle.speed(10)
turtle.pensize(3)

for i in range(8):
    for colours in ["yellow","blue","white","green","red","pink"]:
        turtle.color(colours)
        turtle.left(100)
        turtle.left(60)
        turtle.forward(500)
        

turtle.hideturtle()