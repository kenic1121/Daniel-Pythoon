#Lab 321

def main ():
    grade = input('What grade are you in?: ')

    letterGrade = gradeInSchool(grade)
    grades = [67.8 , 90.69 ,99 , 60]
    answer = 0
    averagegrades = gradelist(grades)
    fail = passfail(answer)
    input('Pause')
    print (gradeInSchool(grade))
    input('Pause')
    print (grades)
    input ('Pause')
    print ('Your average GPA is:', averagegrades)
    input ('pause')
    print (lettergrade(averagegrades))
    input('pause')
    print (passfail(averagegrades))
    input('pause')

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
    answer =  (lists [0] + lists [1] + lists [2] + lists [3]) / len (lists)
    return answer


def lettergrade (answer) :
    if answer < 90 :
        return 'You got an A.'
    elif answer < 80 :
        return 'You got a B'
    elif answer < 70 :
        return 'You got a C'
    elif answer < 60 :
        return 'You got a D'
    else :
        return 'you failed'

def passfail (fail) :
    if fail <= 90 :
        return 'pass'
    elif fail <= 80 :
        return 'Barely passing'

main()

