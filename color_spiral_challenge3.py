# color_spiral_challenge3.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval(input("Enter a number of sides between 2 and 10: "))
colors = ["darkred", "navajowhite", "cornflowerblue", "sandybrown", "lightgreen",
          "mediumpurple", "gainsboro", "whitesmoke", "lightpink", "lightsteelblue"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
    t.left(90)
