import turtle
from turtle import *
import random
schildi = Turtle()
turtle.colormode(255)
schildi.speed(1000000)

R = 0
G = 0
B = 0
schildi.width(4)
for i in range(73):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.forward(300)
    schildi.left(175)
schildi.penup()
schildi.goto(163, 156)
schildi.pendown()
R = random.randrange(0, 257, 10)
G = random.randrange(0, 257, 10)
B = random.randrange(0, 257, 10)
schildi.color(R, G, B)
schildi.circle(150)
done()