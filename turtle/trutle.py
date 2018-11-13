# ToDos: (You can use the documentation below for the following)
#
# 1) Use a different background color for the screen.  Try red, blue and black.
# 2) Draw a 2 squares and 2 rectangle.
# 2a) Make one of each filled and one 'empty' or not filled.
# 2b) Use different colors for the fill and border or lines


import turtle

t = turtle.Pen()

hexcolor = '#db580d'

turtle.bgcolor(hexcolor)

turtle.pencolor('green')

turtle.speed(0)

def square () :
    turtle.hideturtle()

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    moveT(100 , 100)

    turtle.color('purple')
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

#move the turtle using X and y cordinates and cal it in the function
def moveT(x , y) :

    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()



#draw a rectangle
def rectangle ():
    turtle.color('blue')
    moveT(-100 , 200)
    turtle.forward(50)
    turtle.right (90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)

    moveT(-100, -100)

    turtle.color('red')
    turtle.forward(50)
    turtle.right (90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)

    turtle.exitonclick()
square()
rectangle()
