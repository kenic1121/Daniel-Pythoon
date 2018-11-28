import turtle

t=turtle.Pen()


def main():
    color = input('What is the color?:')

    turtle.pencolor(color)

    sidelength = input('What is the side length? ')

    sides = input('How many sides do you want? : ')

    for u in range (0, int(sides)) :
        turtle.forward(int(sidelength))
        turtle.left(float(360) / int(sides))

k


main()
turtle.exitonclick()
