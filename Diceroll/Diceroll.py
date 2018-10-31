import random

def main () :
    setOfDice=[0] * 6
    setOfDice = definedice()
    play = 'y'
    game = 0
    while play == 'y' :
        for i in range (0,22) :
            print ('_', end='')
        print ()
        game += 1
        print (' game - ' + str(game))
        play = input('play again -y or -n ')
    print ('You played ' + str(game) + ' times.')



def definedice () :
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
        elif num == 2:
            dice[num]= [topbot,oneDotL, oneDotM,oneDotR,topbot]
        elif num == 3:
            dice[num]= [topbot,twoDot,blank,twoDot,topbot]
        elif num == 4:
            dice[num]= [topbot,twoDot,oneDotR,twoDot,topbot]
        else:
            dice[num]= [topbot,twoDot,twoDot,twoDot,topbot]
    return dice

