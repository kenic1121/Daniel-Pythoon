def main () :
    string = str (input('Place your word here: '))
    password = deVowel(string)
    epic = [1 ,2 , 3 , 4]
    addnum = 4
    pass2 = mathstuff(epic, addnum)

    print (string)
    print (password)
    print (pass2)


def deVowel(word):
    List = list(word)
    Vowels = ["a", "e", "i", "o", "u"]
    for letter in List:
        if letter.lower() in Vowels:
            List.remove(letter)
    word = ''.join(List)
    return word

def mathstuff(epicmath, multiply) :
    list2 = []
    for i in range( len(epicmath)):
        maththing = epicmath.pop() * multiply
        list2.append(maththing)
    return list2



main()
