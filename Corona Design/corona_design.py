import turtle

t=turtle.Turtle() 
s = turtle.Screen() # Creating turtle screen
s.bgcolor("black") # we can modify the background color of the screen
t.pencolor("green") # Change the pen color


a=0
b=0
t.speed(10)
t.penup()
t.goto(0,200)
t.pendown()


while True:
    t.forward(a) #It moves the turtle in the forward direction by a certain distance.
    t.right(b) #This method moves the turtle right by "b" angle units.
    a+=3
    b+=1

    if b==210:
        break
    t.hideturtle()

turtle.done()
