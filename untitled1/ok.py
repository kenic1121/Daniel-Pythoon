from random import shuffle
word = input('What is your word?:   ')
def shuffle_word(word):

    shuffle(word)
    return ''.join(word)

shuffle_word()
