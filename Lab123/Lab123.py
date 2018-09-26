
def main ():
    grade = input('What grade are you in?: ')
    letterGrade = gradeInSchool(grade)
    print (letterGrade)


def list () :
    intro = input('Type anything to find your average grade: ')
    gradelist = [86.5 , 75.3 , 98.9 , 100]
    p = gradelist[0]
    p1 = gradelist[1]
    p2 = gradelist[2]
    p3 = gradelist[3]
    length = len(gradelist)
    add = (p + p1 + p2 + p3)
    print (intro)
    print (add / length)

#def lettergrade () :
#    if

def gradeInSchool (mynumber) :
    if mynumber == ('9')  :
        return 'Freshman'


    elif mynumber == ('10') :
        print ('You are a sophomore.')

    elif mynumber == ('11')   :
        print ('You are a Junior.')

    elif mynumber == ('12')   :
        print ('You are a senior.')

    else :
        print ('You arent in highschool')

main()



