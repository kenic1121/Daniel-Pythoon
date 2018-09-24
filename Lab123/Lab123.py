from typing import List, Union


def main ():
    grade = input('What grade are you in?: ')

    if grade == ('9')  :
        print ('You are a Freshman.')

    elif grade == ('10') :
        print ('You are a sophomore.')

    elif grade == ('11')   :
        print ('You are a Junior.')

    elif grade == ('12')   :
        print ('You are a senior.')

    else :
        print ('You arent in highschool')

def list () :
    gradelist = [86.5 , 75.3 , 98.9 , 100, 83.6]
    pop = gradelist[1]
    pop1 = gradelist[2]
    pop3 = gradelist[3]
    pop4 = gradelist[4]
    pop5 = gradelist[0]
    print(pop + pop1 + pop3 + pop4 + pop5)



list()
#main()

