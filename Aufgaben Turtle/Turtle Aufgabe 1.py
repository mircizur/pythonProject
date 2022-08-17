from turtle import *
from random import *
zufall = Random()
anzahl = int(input("Bitte eine Zahl eingeben : "))
schildi = Turtle()
schildi.speed(1000)
schildi.width(10)
for z in range(anzahl):
    x = zufall.randint(-700, 701)
    y = zufall.randint(-300, 301)
    zahl = zufall.randint(5, 101)
    schildi.circle(zahl)
    schildi.penup()
    schildi.goto(x,y)
    schildi.pendown()
done()