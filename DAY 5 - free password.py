import random
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
n=['0','1','2','3','4','5','6','7','8','9']
s=['!','#','$','%','&','(',')','*','@']
print('Welcome to my password generator fill in the details for the password you would like to have')
print('How many letters would you like?')
letters=int(input())
print('How many numbers would you like?')
numbers=int(input())
print('How many symbols would you like')
symbols=int(input())
#password=''
#word=''
#for i in range(1,letters + 1):
 #   password+=random.choice(l)
#for i in range(1,numbers + 1):
 #   password+=random.choice(n)
#for i in range(1,symbols + 1):
 #   password+=random.choice(s)
#for i in range(0,len(password)):
  #  word+=random.choice(password)
#print(word)

password=[]
for i in range(1,letters + 1):
    password.append(random.choice(l))
for i in range(1,numbers + 1):
    password.append(random.choice(n))
for i in range(1,symbols + 1):
    password.append(random.choice(s))
print(password)
p=random.shuffle(password)
print(password)
word=''
for i in password:
    word+=i
print(f'Your brand new password is {word}.')
