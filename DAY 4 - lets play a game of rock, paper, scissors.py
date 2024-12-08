import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Hey bro which one are you going for type 0 for rock, type 1 for paper and type 2 for scissors')
x=int(input())
ran=random.randint(0,2)
if x==0:
    print(rock)
    print('computers turn')
    if ran==0:
        print(rock)
    elif ran==1:
        print(paper)
    else:
        print(scissors)
elif x==1:
    print(paper)
    print('computers turn')
    if ran == 0:
        print(rock)
    elif ran == 1:
        print(paper)
    else:
        print(scissors)
elif x==2:
    print(scissors)
    print('computers turn')
    if ran == 0:
        print(rock)
    elif ran == 1:
        print(paper)
    else:
        print(scissors)
else:
    print('wrong number')
if x==ran:
    print('draw')
elif x==0 and ran==1:
    print('lose')
elif x==0 and ran==2:
    print('win')
elif x==1 and ran==0:
    print('win')
elif x==1 and ran==2:
    print('lose')
elif x==2 and ran==0:
    print('lose')
elif x==2 and ran==1:
    print('win')

