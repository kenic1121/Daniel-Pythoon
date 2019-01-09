import turtle
turtle.screensize(1000,1500)
turtle.bgpic("gif.gif")

print("_________Instructions__________")
print("Use the left and right arrow keys to make your way through the maze.")
print("Press the up arrow to reset the game.")
turtle.speed(1)
in_motion = False

def stopMovingTurtle():
    global in_motion
    in_motion = False


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
turtle.onkey(stopMovingTurtle, 'Return')


while True:
   bob.fd(1)
