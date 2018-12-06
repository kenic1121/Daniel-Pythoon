TextCodes = {'think' : 'have a particular opinion, belief, or idea about someone or something.', 'ear' : 'the organ of hearing and balance in humans and other vertebrates' , 'fly' : ' move through the air under control.' }





def checker () :
    yes = 'true'
    while yes == "true":
        answer = input("Name a text code - ")

        if answer == 'main' :
            main()

    word = input('What work would you like to check?   ')
    TextCodes[word]

def changer () :
    yes = 'true'
    while yes == 'true':
        input('What word would you like to change?  ')



def main () :
    cdc = input('Would you like to change, delete, or look at (check) a word?   ')

    if cdc == 'check' :
        checker(TextCodes)

#    elif cdc == 'change' :
 #       changer (TextCodes)

  #  elif cdc == 'delete' :
   #    deleter (TextCodes)


main(TextCodes)
