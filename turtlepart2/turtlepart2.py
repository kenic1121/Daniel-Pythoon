import turtle

t=turtle.Pen()


def main () :
    color = input('What is the color?: ')

    turtle.pencolor(color)

    sidelength = input('What is the side length?:  ')

    turtle.forward(sidelength)


main()
turtle.exitonclick()
