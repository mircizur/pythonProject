import random
from turtle import *
schildi = Turtle()
schildi.speed(1000000)
R = 0
G = 0
B = 0
for a in range(4):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.forward(500)
    schildi.left(90)

for b in range(10, 501, 10):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(0, 0)
    schildi.pendown()
    schildi.goto(500, b)
    schildi.penup()
for c in range(490, 0, -10):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(0, 0)
    schildi.pendown()
    schildi.goto(c, 500)
    schildi.penup()

for d in range(10, 501, 10):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(500, 0)
    schildi.pendown()
    schildi.goto(0, d)
    schildi.penup()
for e in range(10, 501, 10):
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    schildi.color(R, G, B)
    schildi.goto(500, 0)
    schildi.pendown()
    schildi.goto(e, 500)
    schildi.penup()
done()