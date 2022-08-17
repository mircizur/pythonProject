import turtle
from turtle import *
import random
turtle.colormode(255)
R = 0
G = 0
B = 0
schildi = Turtle()
schildi.speed(100000000)
schildi.penup()
schildi.goto(-500, -500)
schildi.pendown()
for a in range(4):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.forward(1000)
    schildi.left(90)

for b in range(-500, 501, 5):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(-500, -500)
    schildi.pendown()
    schildi.goto(500, b)
    schildi.penup()

for c in range(500, -500, -5):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(-500, -500)
    schildi.pendown()
    schildi.goto(c, 500)
    schildi.penup()

for d in range(-500, 501, 5):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(500, -500)
    schildi.pendown()
    schildi.goto(-500, d)
    schildi.penup()

for e in range(-500, 501, 5):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(500, -500)
    schildi.pendown()
    schildi.goto(e, 500)
    schildi.penup()
done()