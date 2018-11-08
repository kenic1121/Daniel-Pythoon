import random

def main () :
   # setOfDice=[0] * 6
 #   for die in range (0,6) :
 #       setOfDice[die] = definedice(die)
  #  print(setOfDice)

    play = 'y'
    game = 0


    while play == 'y' :
        for i in range (0,22) :
            print ('_', end='')
        print()
        roll1 = rollDice()
        roll2 = rollDice()
        definedice(roll1,roll2)


     #   dieroll = definedice(roll)
       # printMyDie(dieroll)
      #  printDiceSideBySide(mydice)

        game += 1
        print (' game - ' + str(game))
        play = input('play again -y or -n ')

    print ('You played ' + str(game) + ' times.')




def definedice (myRoll1 ,myRoll2) :
    dice = [0] * 6
    topbot = ' ------- '
    blank =  '|       |'
    oneDotL= '| *     |'
    oneDotM= '|  *    |'
    oneDotR= '|    *  |'
    twoDot=  '|  * *  |'

    for num in range (0,6):
        if num == 0:
            dice[num]= [topbot,blank,oneDotM,blank,topbot]
        elif num == 1:
            dice[num] = [topbot,blank, twoDot, blank,topbot]
        elif num == 2 :
            dice[num]= [topbot,oneDotL, oneDotM,oneDotR,topbot]
        elif num == 3:
            dice[num]= [topbot,twoDot,blank,twoDot,topbot]
        elif num == 4:
            dice[num]= [topbot,twoDot,oneDotM,twoDot,topbot]
        else:
            dice[num]= [topbot,twoDot,twoDot,twoDot,topbot]
    for row in range (0,5):
        print (dice[myRoll1][row],dice[myRoll2][row])


def rollDice() :
    diceNum = random.randint(0 , 5)
    return diceNum

def printMyDie (myDieRoll) :
    for row in myDieRoll :
        print(row)

def printDiceSideBySide(diceSet) :
    print('print dice')
    for row in range (0 , 0):
        for col in range (0 , 0):
            print(diceSet[col][row] , end = '/t')
        print()
    return diceSet

main()
