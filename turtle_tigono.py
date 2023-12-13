import turtle
import math


t = turtle.Turtle()
t.showturtle()
#t.speed(0)  # Set the drawing speed (0 is the fastest)

# Set up the coordinate system
t.penup()
t.goto(-360, -100)
t.pendown()

# Plot the sine function in red
t.pencolor("red")
for x in range(-360, 361):
    y = math.sin(math.radians(x))
    t.goto(x, y * 100)

# Move to a new starting position for the cosine function
t.penup()
t.goto(-360, -100)
t.pendown()

# Plot the cosine function in blue
t.pencolor("blue")
for x in range(-360, 361):
    y = math.cos(math.radians(x))
    t.goto(x, y * 100)

# Close the turtle graphics window on click
screen.exitonclick()