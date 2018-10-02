def scool ():
    print ('Bellarmine')
    print ('python')




def yearschoolgrade ():

    grade = input('What is your grade?:  ')
    yearschool = (int(grade) + 0)

    print ('You ave been going to school for ' + str(yearschool) + ' Years')




from random import *

def ran () :
    x = input ('What is the first number?: ')
    y = input ('What is the second number?: ')
    num = randint (int(x), int (y))

    print (str(num) + ' is a random number between')
    print (str(x) + ' and ' + str(y))




def gradecity () :
    grade = input ('What grade are you in?: ')
    city = input ('What is your city?: ')

    print (grade)
    print (city)



def areabox () :
    x = input('What is the vertical line in inches: ')
    y = input('What is the horrizontal line in inches: ')
    print ('The area of the box is: ')
    print (int (x) * int(y))




def perimbox () :
    x = input ('What is the vertical line in inches: ')
    y = input ('What is the horrizonal line in inches: ')
    print ('The perimeter of your box is: ')
    print (int(x) + int(x) + int(y) + int(y))


scool ()
yearschoolgrade ()
ran()
gradecity()
areabox()
perimbox()
