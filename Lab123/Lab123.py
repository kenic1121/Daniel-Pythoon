
def main ():
    grade = input('What grade are you in?: ')

    letterGrade = gradeInSchool(grade)
    grades = [67.8 , 89.9 ,99 , 100]
    averagegrade = gradelist(grades)
    print (letterGrade)
    


def gradeInSchool (mynumber) :
    if mynumber == ('9')  :
        return 'Freshman'


    elif mynumber == ('10') :
        return 'Sophmore'
    elif mynumber == ('11')   :
        return 'Junior'

    elif mynumber == ('12')   :
        return 'Senior'

    else :
        return 'You arent in high school.'

def gradelist (lists) :
    answer = 0
    print (lists)
    print ('Your average GPA is: ')
    answer =  (lists [0] + lists [1] + lists [2] + lists [3]) / len (lists)


    print (answer)




main()



