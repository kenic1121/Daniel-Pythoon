import turtle
from tkinter import *

def text ():
    root = Tk()
    T = Text(root, height=25, width=100)
    T.pack()
    T.insert(END, "_________Instructions__________ \n1. Use the left and right arrow keys to make your way through the maze.\n2. Press the up arrow to reset the game.\n3. Stay in the lines\n\n\n\nTo start the game close this window and make the game full screen.")
    mainloop()





def turtleMove () :
    turtle.screensize(300,600)
    turtle.bgpic("gif.gif")
    print("_________Instructions__________")
    print("Use the left and right arrow keys to make your way through the maze.")
    print("Press the up arrow to reset the game.")
    turtle.speed(1)

    def rightTurn():
       bob.rt(90)

    def leftTurn():
       bob.lt(90)

    def up() :
        bob.reset()

    wn=turtle.Screen()
    wn.bgcolor('lightblue')

    bob=turtle.Turtle()

    wn.onkeypress(rightTurn, "Right")
    wn.onkeypress(leftTurn, "Left")
    wn.onkeypress(up, "Up")
    wn.listen()


    while True:
       bob.fd(1)



text()
turtleMove()
