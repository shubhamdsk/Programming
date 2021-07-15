# Clock Design

import turtle
import time

screen = turtle.Screen() #turtle screen
screen.bgcolor("black") #background of the screen
screen.setup(width=600, height=600) #geometry of the GUI
screen.title("Ghadi") #title of the GUI
screen.tracer(0) #tracer for the GUI

kalam = turtle.Turtle() #the turtle
kalam.hideturtle() #make the turtle invisible
kalam.speed(0) #setting the speed to 0
kalam.pensize(3) #setting the pensize to 3


def ghadi_bana(ghantaa, minutee, secondd, kalam): #function with 4 parameters

    kalam.up() #not ready to draw
    kalam.goto(0, 210) #positioning the turtle
    kalam.setheading(180) #setting the heading to 180
    kalam.color("red") #setting the color of the pen to red
    kalam.pendown() #starting to draw
    kalam.circle(210) #a circle with the radius 210

    kalam.up() #not ready to draw
    kalam.goto(0, 0) #positioning the turtle
    kalam.setheading(90) #same as seth(90) in newer version

    for z in range(12): #loop 
        kalam.fd(190) #moving forward at 190 units
        kalam.pendown() #starting to draw
        kalam.fd(20) #forward at 20
        kalam.penup() #not ready to draw
        kalam.goto(0, 0) #positioning the turtle
        kalam.rt(30) #right at an angle of 30 degrees

    hands = [("white", 80, 12), ("white", 150, 60), ("white", 110, 60)] #the color and the hands set
    time_set = (ghantaa, minutee, secondd) #setting the time

    for hand in hands: #loop
        time_part = time_set[hands.index(hand)] #time part in the hand index in hands of time_Set
        angle = (time_part/hand[2])*360 #setting the angle for the clock
        kalam.penup() #not ready to draw
        kalam.goto(0, 0) #positioning the turtle
        kalam.color(hand[0]) #setting the color of the hand
        kalam.setheading(90) #same as seth(90)
        kalam.rt(angle) #right at an angle of "right"
        kalam.pendown() #ready to draw
        kalam.fd(hand[1]) #forward at a unit of 1st index of the hand var


while True:
    ghantaa = int(time.strftime("%I")) #setting the hour from the time module
    minutee = int(time.strftime("%M")) #setting the minute from the time module
    secondd = int(time.strftime("%S")) #setting the second as above

    ghadi_bana(ghantaa, minutee, secondd, kalam) #calling the ghanta_bana() function with the given parameters
    screen.update() #updating the scren
    time.sleep(1) #making the code sleep for a second with the time module
    kalam.clear() #clearing the pen