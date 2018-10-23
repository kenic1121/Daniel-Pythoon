def main () :
    string = str (input('Place your word here: '))
    password = deVowel(string)


    print (string)
    
    print (password)


def deVowel(word):
    List = list(word)
    Vowels = ["a", "e", "i", "o", "u"]
    for letter in List:
        if letter.lower() in Vowels:
            List.remove(letter)
    word = ''.join(List)
    return word



main()
