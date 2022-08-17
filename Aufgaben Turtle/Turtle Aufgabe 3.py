from turtle import *
ecken = int(input("Anzahl Ecken? : "))
xeck = Turtle()
for i in range(ecken):
    xeck.forward(100)
    xeck.right(360 / ecken)
done()