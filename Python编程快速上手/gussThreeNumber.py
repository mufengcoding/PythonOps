# This is a guss number game!

from random import *

answerNum = randint(1, 20)
print('I am thinking of a number between 1 and 20')

for i in range(1, 5):
    guss = int(input())
    if guss > answerNum:
        print('Your guss is too high')
    elif guss < answerNum:
        print('Your guss is too low')
    else:
        break
if guss == answerNum:
    print('Good job in ' + str(i) + ' gusses!')
else:
    print('The answer is :' + str(answerNum))
