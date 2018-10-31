def main () :
    shoppingcart = [['tooth paste' , 'q-tips' , 'milk'] , ['milk' , 'candy' , 'apples'] ,['paper' , 'pencils' , 'q-tips']]
    print(allInOne(shoppingcart))
    input ('Pause')
    print ('There are ' , countQtips(shoppingcart), 'Q-tips in the cart.')
    input ('Pause')
    print (drinkMoreMilk(shoppingcart))
    input('Pause')
    print (mooseCookie(shoppingcart))

def allInOne(cart):
    newList = []
    for list in cart:
        for item in list:
            if item not in newList:
                newList.append(item)
    return newList

def countQtips(cart):
    newerList = []
    count = 0
    for list in cart:
        for item in list:
            if item not in cart:
                newerList.append(item)
    for i in range(len(newerList)):
        if newerList[i] == 'q-tips':
            count += 1
    return count

def drinkMoreMilk (cart) :
    for list in cart :
        for item in list :
            if 'milk' not in list :
                list.append('milk')
    return (cart)

def mooseCookie (cart) :
    for list in cart :
        for item in list :
            if 'milk' in list :
                list.remove ('milk')
                list.append ('milk and cookies')
    return cart


main()
