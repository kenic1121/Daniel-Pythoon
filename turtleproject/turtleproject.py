import turtle

t=turtle.Pen()

#turtle.bgpic('ok2.gif')
turtle.bgcolor('green')




#Move the pen
def moveT (x , y) :
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()

def lineT () :
    moveT(-50 , 0)
    turtle.pencolor('red')
    turtle.forward(100)

def square () :
    moveT(-100 , 100)
    hexcolor = '#ff0061'
    turtle.pencolor(hexcolor)

    for i in range (0 ,4) :
        turtle.forward(200)
        turtle.right(90)


def circle () :
    moveT(0 , -300)

    turtle.pencolor('black')

    turtle.circle(300)

def triangle () :
    moveT(-200 , -150)

    turtle.color(0.5 , 0.6 , 0)

    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)

lineT()
square()
circle()
triangle()
turtle.exitonclick()
