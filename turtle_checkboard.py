import turtle


turtle.showturtle()
turtle.penup()
turtle.goto(0,320)
turtle.pendown()
row = 1
y=320



for row in range(1,9):
 for i in range(1,5):
    for j in range (1,5):
     turtle.forward(10)
     turtle.right(90)
    turtle.forward(10)
    for k in range(1, 5):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(10)
        turtle.right(90)
        turtle.end_fill()
    turtle.forward(10)
 turtle.penup()
 row += 1
 y = y-10
 turtle.goto(0,y)
 turtle.pendown()
 row += 1
turtle.done()


#Somehow the alternate square is not getting filled with black