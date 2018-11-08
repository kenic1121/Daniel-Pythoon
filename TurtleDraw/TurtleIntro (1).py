# Welcome to Graphics!
#

# The Python language has no idea about graphics, drawing to the screen or creating and editing images.
# Those are things most operating systems can do - and they provide interfaces or frameworks for other
# apps to use to do those things.

# In Python, we use these operating system capabilities thru code or libraries that
# others have created to simplify the task.

# There are several options for graphics programming depending on what you want to do.
# You usually choose the library based on what you want to do.  You would not use the same
# library for creating and editing image files as you would for writing a 2 or 3D video game.
# One mostly edits files stored on the computer's hard drive while the other draws to the computer screen.
# And may also keep track of things like, where the user clicked the mouse.

# One of the most popular libraries for learning computer drawing in Python is called Turtle Graphics.
# Turtle is packaged with most Python versions - which is one reason why its popular.
# Its also easy to use and understand. But just remember, its not part of Python itself.

# In this class, we're going to learn some basic graphics programming with Turtle Graphics,
# and then move on to another graphics library that do things like animations and sound --
# basically what you'd need for creating games and/or other kinds of apps.

# Turtle Graphics
# Turtle is a simple library (shared code we can use) for doing 2D image programming.
# While its simple to use, you can use it to create some pretty cool computer drawings.

# Getting Started
# To use Turtle, we have to import it into our Python file.

# That looks like this.
import turtle

# Turtle works with the concept of a virtual pen.  You move the
# pen around the screen and draw where the pen is 'pointing'.
# Turtle can also draw circles and a few more shapes - but mostly
# you draw by moving the virtual pen around the screen.

# Just like a real pen, you can by putting the pen 'down'
# and moving it - and picking it 'up' when you don't want to draw.

# By default, Turtle will draw an arrow at the current position
# that points in the drawing direction.  You can also hide this
# arrow if you don't want to include it in your drawing.

# To create a pen and show it in the default position (centered), you'd
# just write.
pen = turtle.Pen()

# To see what you can do with some simple commands,
# try to visualize what this method does.
def mystery_drawing_one(angle):
    for x in range(100):
        pen.forward(x)
        pen.left(angle)


# Can you tell? Uncomment below to see.
#mystery_drawing_one(90)

# Imagine a slight change to the last - what if we change the angle
# by 91 deg. instead of 90.
#mystery_drawing_one(91)

# You can also set the pen color.
#pen.pencolor("red")
#mystery_drawing_one(91)

# Turtle has some built in named colors you would expect, like
# red, blue, green etc..
# You can also create your own colors using web style 'hex' colors
# or using RGB colors.

# RGB stands for Red, Green, Blue and its created by 'mixing' values
# for each of those 3 base colors where each base can be a
# number from 0.0 to 1.0.
black_color = (0.0, 0.0, 0.0)
white_color = (1.0, 1.0, 1.0)
red_color = (1.0, 0.0, 0.0)
green_color = (0.0, 1.0, 0.0)
blue_color = (0.0, 0.0, 1.0)
hex_color = "#ffe063"

#############turtle.bgcolor("green")
#turtle.bgpic("tenor.gif")
turtle.register_shape (“name_of_file.gif”)

# Use like so:
pen.pencolor(blue_color)
mystery_drawing_one(91)

# Note that Turtle doesn't really have a 'color' object.  You would
# create and store colors as I did above - with a tuple of 3 integers
# or a hex string color. (See below for more on color).
#pen.pencolor(hex_color)
#pen.pencolor(blue_color)
#mystery_drawing_one(80)

# Additional Turtle Info
#
# Specify a screen size and/or start position
#turtle.setup(width=600, height=500)

# Moving the pen
#
# turtle.forward(10)
# turtle.backward(10)
# turtle.left(10)
# turtle.right(10)
# turtle.setx(10)
# turtle.sety(10)
# turtle.goto(10, 10)
# turtle.setpos(10, 10) # same as goto()

# Move the arrow/turtle back to the beginning (origin)
# turtle.home()

# Clear the screen and return to the origin
# turtle.reset()

# Hide/show the arrow (turtle) while printing
# turtle.hideturtle()
# turtle.showturtle()

# Set drawing (animation) speed; 0 means no animation
# turtle.setspeed(0)

# Get screen size info
# turtle.window_height()
# turtle.window_width()

# Set a title
# turtle.title("My Drawing")

# Finish with this - it tells Turtle to pause until
# you close.  Otherwise, it'd just draw your image then quit.
turtle.exitonclick()

#
# ToDos: (You can use the documentation below for the following)
#
# 1) Use a different background color for the screen.  Try red, blue and black.
# 2) Draw a 2 squares and 2 rectangle.
# 2a) Make one of each filled and one 'empty' or not filled.
# 2b) Use different colors for the fill and border or lines

#
# Documentation
# Turtle Graphics - https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

#
# Geek-down on color:  ¯\_(ツ)_/¯
#
# There are several different systems for creating colors
# RGB and RGBA are probably the most popular.  You've already seen
# RGB - RGBA just adds another variable for alpha (A) or transparency
# Even within RGB/RGBA there are options - some sytems encode the color
# as number up to 256 (CHAR datatype in some languages like Java).
# And some encode the color as a decimal number between 0.0 and 1.0
# And actually, Turtle can handle either encoding.
# Hex or Hexadecimal (which means 16 or base 16) is very popular in web development and HTML/CSS.

# A Hex color usually looks something like: #ffe063
# The hash or # sign indicates its a hexadecimal number.
# Remember when I said some RGB systems use a number between 0 and 255 (256 range)?
# Actually, hex colors are RGB colors.
# Hex numbers are base 16 (vs base 10 in decimal).  We don't want
# 2 digits in the number.  So how do we represent numbers greater than 9?
# With letters.  In hex - 0 - 9 are just like and have the same value
# as decimal -- and the numbers 10 - 15 (there is no 16 because it starts at 0
# and goes to 15 for a range of 16 -- like decimal goes from 0 to 9) start at 'a' or 'A'
# and go to 'f' or 'F' for 15.  ('A' = 10; 'B' = 11; ... 'F' = 15)
#
# Looking at the hex color above - like decimal -- every place is a power of the base number - 16 in this case.
# And the number is arranged in pairs of digits. And its basically an RGB value.
# ff = red part; e0 = green part; 63 = blue part
# Now that we know hoe to decode hex, we can convert these to their decimal parts.
# ff = (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255 -- which is the highest number in the integer scale
# e0 = (14 * 16^1) + (0 * 16^1) = 224 + 0 = 224
# 63 = (6 * 16^1) + (3 * 16^0) = 96 + 3 = 99
# So, the hex color #ffe063 = (255, 224, 99) in standard RGB
# There are lots of color converters on the web you can use to experiment with this.

# We won't go too much into color theory in this class, but just understand its a very rich topic
# and there are other colors schemes used in digital printing, photography, Home Depot paint colors, etc...
# Each one with a different strength.  Why so many, because real color in the world is much broader
# than we humans can see or appreciate.  Colors go further into the electro-magnetic spectrum than humans can
# see.  So any system that codes colors for humans is going to have trade-offs.
# And different color encodings have been created to do different jobs.
# RGB / RGBA is by far the most popular in general computing.
#
# But there others that you might come across such as:  HSL (hue, saturation and luminosity or lightness) and
# CMYK (cyan, magenta, yellow and key).
#
# The only other thing to know is that color systems can also be classified as additive or subtractive.
# As the names imply, in an additive system -- you add color into to form the color and in subtractive you subtract.
# Computers and monitors and tv's are examples of additive color.  So RGB is an additive scheme.
# CMYK is an example of a subtractive system and is widely used in the print industry.  Usually 'real-world' colors,
# like paint and ink are subtractive and virtual or computer systems are additive.
#
# How many colors could we create with the 256 type RGB scheme?
# 256^3 = 256 * 256 * 256 = 16,777,216 colors!
