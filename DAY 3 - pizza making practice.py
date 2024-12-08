print('The small pizza size is $15')
print('The medium pizza size is $20')
print('The large pizza size is $25')
b=input('So which one do you want to order')
if b=='s'or'$15':
    print('Should we add pepperoni on small pizza for $2')
    sp=input('y or n')
    bill=15
    if sp=='y':
        bill+=2
elif b == 'm'or'$20':
    print('Should we add pepperoni on medium pizza for $3')
    mp = input('y or n')
    bill=20
    if mp == 'y':
        bill += 3
else:
    print('Should we add pepperoni on large pizza for $3')
    lp = input('y or n')
    bill=25
    if lp == 'y':
        bill += 3
a=input('Do you want extra cheese on your pizza(y or n)')
if a=='y':
    print(bill+1)
else:
    print(bill)




