from turtle import *
schildi = Turtle()
schildi.speed(1000000)
for a in range(4):
    schildi.forward(500)
    schildi.left(90)

for b in range(5, 501, 5):
    schildi.goto(0, 0)
    schildi.pendown()
    schildi.goto(500, b)
    schildi.penup()
for c in range(495, 0, -5):
    schildi.goto(0, 0)
    schildi.pendown()
    schildi.goto(c, 500)
    schildi.penup()

for d in range(5, 501, 5):
    schildi.goto(500, 0)
    schildi.pendown()
    schildi.goto(0, d)
    schildi.penup()
for e in range(5, 501, 5):
    schildi.goto(500, 0)
    schildi.pendown()
    schildi.goto(e, 500)
    schildi.penup()
done()