
import random
import sys
print('')
print(' ROCK,PAPER,SCISSORS GAME')
w, l, t = [0,0,0]
gamersMove = ''
compMove = ''

while True:

    # computer makes a guess
    randNumber = random.randint(1,3)
    if randNumber == 1:
        compMove = 'r'
    elif randNumber == 2:
        compMove = 's'
    elif randNumber == 3:
        compMove = 'p'

    # player makes a guess
    print('')
    print(str(w) + ' Wins, ' + str(l) + ' Losses, ' +  str(t) + ' Ties.')
    while True:
        print('Enter your move: (r)ock, (s)cissors, (p)aper or (q)uit. ')
        gamersMove = input().lower()
        if gamersMove == 'q':
            sys.exit()
        elif gamersMove in ('rsp'):
            break
        else:
            print('You entered wrong letter. try again!')
            continue

    #Compare the two
    if compMove == 'r':
        if gamersMove == 'r':
            print('Mine was rock too. Dang. It is a Tie')
            t += 1
        elif gamersMove == 's':
            print('Mine was Rock. You Loose. hahaha')
            l += 1
        else:
            print('Dang You won. Mine was Rock. Try again')
            w +=1
            continue

    if compMove == 's':
        if gamersMove == 's':
            print('Mine was rock too. Dang. It is a Tie')
            t += 1
        elif gamersMove == 'p':
            print('Mine was Scissors. You Loose. hahaha')
            l += 1
        else:
            print('Dang You won. Mine was Scissors. Try again')
            w +=1
            continue

    if compMove == 'p':
        if gamersMove == 'p':
            print('Mine was rock too. Dang. It is a Tie')
            t += 1
        elif gamersMove == 'r':
            print('Mine was Paper. You Loose. hahaha')
            l += 1
        else:
            print('Dang You won dude. Mine was Paper. Try again')
            w +=1
            continue

