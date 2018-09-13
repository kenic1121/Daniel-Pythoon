
print ('My List:')
numlist = [1,2,3,4,5,6,7,8,9,10]
print (numlist)

print ('Counts all thenumbers and adds them up:')
print (len(numlist))

print ('Get first 5 numbers:')

sublist = numlist[0:5]
print (sublist)



print ('Insert 3 into list:')
sublist.insert (0 , 3)
print (sublist)

print ('Inserts a nummber:')

sublist2 = sublist + [6]
print (sublist2)


print('My Classes:')

classes = ['flee' , 'tree' , 'sight']
print (classes)

print ('Remove a class:')

classes.remove('tree')
print (classes)

print ('Pop a class:')

favclass = classes.pop (0)
print (classes)

print ('My favorite class is' , favclass)
