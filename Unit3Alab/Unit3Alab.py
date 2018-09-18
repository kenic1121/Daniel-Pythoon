def scool ():
    print ('Bellarmine')
    print ('python')

scool ()


def yearschoolgrade ():

    grade = input('What is your grade?:  ')
    yearschool = (int(grade) + 0)

    print ('You ave been going to school for ' + str(yearschool) + ' Years')

yearschoolgrade ()


from random import *

def ran () :
    x = input ('What is the first number?: ')
    y = input ('What is the second number?: ')
    num = randint (int(x), int (y))

    print (str(num) + ' is a random number between')
    print (str(x) + ' and ' + str(y))

ran()



