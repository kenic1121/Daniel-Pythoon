calcnum1 = input ('1st number to calculate: ')
calcnum2 = input ('2nd number to calculate: ')
sign = input ('Would you like to multiply (*), Divide (/), subtract (-), or add (+):')


print (calcnum1)
print (sign)
print (calcnum2)



if sign == ("*") :
    print (int(calcnum1) * int(calcnum2))

elif sign == ("/") :
    print (int(calcnum1) / int(calcnum2))

elif sign == ("-") :
    print (int(calcnum1) - int(calcnum2))

elif sign == ("+") :
    print (int(calcnum1) + int(calcnum2))

else :
    print ('ERROR')
