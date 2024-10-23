import turtle
import random
colours = ["cyan", "purple", "white", "red", "yellow", "green"]
pat = turtle.Turtle()
turtle.Screen().bgcolor("black")
r = 50
pat.color("white")
pat.circle(r)

pat.penup()
pat.left(90)
pat.forward(50)
pat.pendown()

for i in range(10):
    pat.color(random.choice(colours))
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.right(36)
