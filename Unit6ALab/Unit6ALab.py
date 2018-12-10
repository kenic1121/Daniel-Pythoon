TextCodes = {'think' : 'have a particular opinion, belief, or idea about someone or something.', 'ear' : 'the organ of hearing and balance in humans and other vertebrates' , 'fly' : ' move through the air under control.' }






def check(TextCodes):
    yes = "true"

    while yes == "true":

        ans = input("Name a word :   ")


        if ans == "menu":
            main(TextCodes)
            return


        if ans in TextCodes:
            print(TextCodes[ans])


        else:
            define = input("What does that mean?")
            if define == "menu":
                main(TextCodes)
                return

            TextCodes[ans] = define

def change(TextCodes):
    go = "true"

    while go == "true":

        print("What word will be changed?: ")
        print(TextCodes)


        key = input("")


        if key == "menu":
                main(TextCodes)
                return


        if key in TextCodes:
            text = input("What change will you make?:  ")
            if text == "menu":
                    main(TextCodes)
                    return


            TextCodes[key] = text


        else:
            print("Word not found.")

def delete(TextCodes):
    go = "true"

    while go == "true":
        print("What would you like to delete?: ")
        print(TextCodes)


        ans = input("")


        if ans == "menu":
            main(TextCodes)
            return


        if ans in TextCodes:
            deleted = TextCodes.pop(ans)
            print(TextCodes)
            print("Finished")


        else:
            print("Word not found, try again")



def main(textCodes):
    wordDecision = input("Would you like to -change -check -delete a word: ")

    print("Type menu to go back to the menu")

    if wordDecision == "check":

        check(textCodes)

    if wordDecision == "change":

        change(textCodes)

    if wordDecision == "delete":

        delete(textCodes)




main(TextCodes)
