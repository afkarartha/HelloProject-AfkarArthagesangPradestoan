# Python program to draw 
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)


##from turtle import *
##left(90)
##pensize(10)
##penup()
##forward(100)
##pendown()
##pencolor("red")
##begin_fill()
##circle(70,230)
##pensize(10)
##pencolor("red")
##
##pencolor("red",)
##forward(140)
##seth(40)
##forward(135)
##pencolor("red")
##right(5)
##circle(70,210)
##pencolor("black")
##
##seth(30)
##fillcolor("red")
##end_fill()
##seth(-90)
##pencolor("red")
##pensize(3)
##forward(50)
##pencolor("black")
##

hideturtle()
done()
