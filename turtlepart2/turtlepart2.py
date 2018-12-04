import turtle
from random import randint
t=turtle.Pen()


def main():
    color = input('What is the color?:')

    turtle.pencolor(color)

    sidelength = input('What is the side length? ')

    sides = input('How many sides do you want? : ')

    for u in range (0, int(sides)) :
        turtle.forward(int(sidelength))
        turtle.left(float(360) / int(sides))




#main()


def moveT (x , y) :
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()


def shapeoneandfour () :
    moveT(150 , 100)
    turtle.pencolor('green')

    for i in range (0,4) :
        turtle.forward(50)
        turtle.left (90)

    moveT(-150 , 100)
    turtle.pencolor('blue')

    for u in range (0 , 6) :
        turtle.forward (50)
        turtle.left (60)

    moveT(-150 , -100)
    turtle.pencolor('purple')

    for e in range (0 , 3) :
        turtle.forward (50)
        turtle.left (120)

    moveT(150 , -150)

    turtle.pencolor('red')

    for h in range (0 , 8) :
        turtle.forward(50)
        turtle.left(45)






#shapeoneandfour()
turtle.speed(0)
def circleart (angle) :
    for g in range (60) :
        moveT(0 , -200)

        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        turtle.color(red / 255, green / 255, blue / 255)

        turtle.circle(angle)
        turtle.left(angle)
        turtle.forward(10)

def circlearttwo (angle) :
    for g in range (90) :
        moveT(0 , 200)

        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        turtle.color(red / 255, green / 255, blue / 255)

        turtle.forward(40)
        turtle.circle(angle)

        turtle.left(angle)


def owndesign (angle) :
    for g in range (10) :

        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        turtle.color(red / 255, green / 255, blue / 255)

        turtle.forward(50)
        turtle.circle(angle)
        turtle.forward(30)

        turtle.left(angle)

    for g in range (15) :

        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        turtle.color(red / 255, green / 255, blue / 255)

        turtle.forward(50)
        turtle.circle(100)
        turtle.forward(30)

        turtle.left(angle)


#circleart(46)
#circlearttwo(91)

owndesign(40)


turtle.exitonclick()
