'''
(Turtle: two circles) Write a program that prompts the user to enter the center
coordinates and radii of two circles and determines whether the second circle is
inside the first or overlaps with the first
'''

import math
import turtle

x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

# Draw circle 1
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.circle(r1)

# Draw circle 2
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.circle(r2)

dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

turtle.penup()
turtle.goto(max(x1 + r1, x2 + r2), max(y1 + r1, y2 + r2))
turtle.pendown()

if dist <= abs(r1 - r2):
    turtle.write("circle2 is inside circle1", font=("Arial", 16, "bold"))
elif dist <= r1 + r2:
    turtle.write("circle2 overlaps circle1", font=("Arial", 16, "bold"))
else:
    turtle.write("circle2 does not overlap circle1", font=("Arial", 16, "bold"))

turtle.done()