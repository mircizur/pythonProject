from turtle import *
schildi = Turtle()
schildi.color("green")
schildi.speed(1000000)
schildi.penup()
schildi.goto(-500, -500)
schildi.pendown()
for a in range(4):
    schildi.forward(1000)
    schildi.left(90)

for b in range(-500, 501, 10):
    schildi.goto(-500, -500)
    schildi.pendown()
    schildi.goto(500, b)
    schildi.penup()
for c in range(500, -500, -10):
    schildi.goto(-500, -500)
    schildi.pendown()
    schildi.goto(c, 500)
    schildi.penup()

for d in range(-500, 501, 10):
    schildi.goto(500, -500)
    schildi.pendown()
    schildi.goto(-500, d)
    schildi.penup()

for e in range(-500, 501, 10):
    schildi.goto(500, -500)
    schildi.pendown()
    schildi.goto(e, 500)
    schildi.penup()
done()