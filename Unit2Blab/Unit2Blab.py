
#note
#x = -5
#use "if" to
#if x > 0:
 #   print ('x is positive')
#use elif if you nneed more
#elif x < 0:
 #   print ('x is negative')
#if "if" is wrong what "else" is it
#else:
 #   print ("x = 0")
from clint.textui.colored import blue

numGrade = input ("Enter your grade here:")
numGrade = int (numGrade)
if numGrade >= 90:
    print ("yahoo you got an A! Congrats!")

elif numGrade >= 80:
    print ("Nice, a B, halfway there")

elif numGrade >= 70:
    print ("do better, a C isnt good enough")

else:
    print ("study more")




color = input ("What is yur favorite color:")

if color == ("blue"):
    print ("The sky is blue")

elif color == ("green"):
    print ("The grass is green")
elif color == ("red"):
    print ("Blood is red")

elif color == ("yellow"):
    print ("A sunflower is yellow")
else:
    print ("There are only 4 colors.")
