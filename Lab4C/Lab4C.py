def draw7 () :
    for i in range (0 , 7):
        for u in range (0 , 7) :
            print ('*' , end='')
        print()

def starsandstripes () :
    for o in range (0 , 3) :
        for i in range(0, 7):
            print('*', end='')
        print()
        for u in range(0, 7):
            print('-', end='')
        print()

def inctriangle () :
    for o in range (1 , 8) :
        for i in  range (0 , o) :
            print(o , end='')
        print()






#draw7()
#starsandstripes()
inctriangle()
