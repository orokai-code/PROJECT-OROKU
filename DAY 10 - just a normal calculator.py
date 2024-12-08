from art import *
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
dic={}
dic['+']=add
dic['-']=sub
dic['*']=mul
dic['/']=div
first = float(input('pls input your first digit pls\n'))
def cal():
    print(logo)
    game = True
    while game:
        for i in dic:
            print(i)
        operate = input('pls select your operation\n')
        second = float(input('pls input another number that you would like to use\n'))
        result = dic[operate](first, second)
        print(f'{first} {operate} {second} = {result}')
        again = input(f'Type Y to continue calculating with {result} or type N to start new calculation\n').lower()
        if again == 'y':
            first = result
        else:
            game = False
            print('\n' * 100)
            cal()
cal()












