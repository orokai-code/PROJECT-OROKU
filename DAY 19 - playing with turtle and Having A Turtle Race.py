from random import *
from turtle import *
race=False
screen=Screen()
screen.setup(width=500,height=400)
user=screen.textinput(title='Make your bet',prompt='Which turtle will win the race. Pls enter a colour')
colors=['red','orange','yellow','green','blue','purple']
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]
for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(new_turtle)
if user:
    race=True
while race:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            race=False
            winning_col=turtle.pencolor()
            if winning_col==user:
                print(f'Bro you just won. {winning_col} turtle is the winner')
            else:
                print(f'Bro you just lost. {winning_col} turtle is the winner')
        ran_d = randint(0, 10)
        turtle. forward(ran_d)
screen.exitonclick()

