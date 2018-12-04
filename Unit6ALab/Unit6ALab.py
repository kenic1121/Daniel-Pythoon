TextCodes = {'think' : 'have a particular opinion, belief, or idea about someone or something.', 'ear' : 'the organ of hearing and balance in humans and other vertebrates' , 'fly' : ' move through the air under control.' }


#prints the deffinition
#print (TextCodes['think'])
search = input('Would you like to search or change a word in the dictionary?    ')

if search == 'search' :
    wordfind = input('What word do you want the deffinition of?    ')

elif search == 'change' :
    input('What word would you like to change?  ')






if wordfind == 'think' :
    print(TextCodes['think'])

elif wordfind == 'ear' :
    print(TextCodes['ear'])

elif wordfind == 'fly' :
    print(TextCodes['fly'])

else :
    newword = input('Is this a new word?  ')




if newword == 'yes' :
   deffinition = input('What is the deffinition of your word?')
   TextCodes[wordfind] = deffinition
elif newword == 'no' :
    input('click any key to exit')
else:
    print('error')


