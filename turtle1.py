#Turtle Clock

import turtle
import time


window = turtle.Screen()
window.title("Digital Clock")
window.bgcolor("white")

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)




def draw_clock(h, m, s):
    #turtle.clear()

    # Display the time in HH:MM:SS format
    time_string = f"{h:02d}:{m:02d}:{s:02d}"
    turtle.penup()
    turtle.goto(0, -250)
    turtle.write(time_string, align="center", font=("Courier", 20, "normal"))

    # Draw the clock hands
    turtle.pensize(2)

    # Hour hand
    turtle.penup()
    turtle.goto(0, -25)
    turtle.setheading(90 - (h % 12) * 30 - (m / 60) * 30)
    turtle.pendown()
    turtle.forward(40)

    # Minute hand
    turtle.penup()
    turtle.goto(0, -25)
    turtle.setheading(90 - m * 6)
    turtle.pendown()
    turtle.forward(60)

    # Second hand
    turtle.penup()
    turtle.goto(0, -25)
    turtle.setheading(90 - s * 6)
    turtle.pendown()
    turtle.forward(70)

    turtle.hideturtle()
    turtle.done()




current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
second = current_time.tm_sec
draw_clock(hour, minute, second)



