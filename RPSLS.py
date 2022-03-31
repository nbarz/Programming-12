
import random
import time

wins = 0
turns = 0
losses = 0
PCguess = None
Guess = None
killGame = False

def rules():
    print('        |RULES|')
    print('Scissors cuts Paper')
    print('')
    print('Paper covers Rock')
    print('')
    print('Rock crushes Lizard')
    print('')
    print('Lizard poisons Spock')
    print('')
    print('Spock smashes Scissors')
    print('')
    print('Scissors decapitates Lizard')
    print('')
    print('Lizard eats Paper')
    print('')
    print('Paper disproves Spock')
    print('')
    print('Spock vaporizes Rock')
    print('')
    print('Rock crushes Scissors')
def load():
    print('BOOTING UP')
    print('')
    time.sleep(.5)
    print('Loading 10%')
    time.sleep(.5)
    print('Loading 15%')
    time.sleep(.5)
    print('Loading 17%')
    time.sleep(.5)
    print('Loading 30%')
    time.sleep(.2)
    print('Loading 50%')
    time.sleep(.2)
    print('Loading 90%')
    time.sleep(1.5)
    print('Loading 93%')
    time.sleep(2)
    print('Loading 100%')
    time.sleep(1)
    print('')
    print('Done!')
    print('')
    print('')
    print('Welcome to |Rock Paper Scissors Lizard Spock|')
def padding():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
def isWin():
    if Guess == 'r' and PCguess == '4' or PCguess == '3':
        if PCguess == '4':
            print(' Your rock flattens the lizard, YOU WIN!')
            
        elif PCguess == '3':
            print(' You take out your anger on the scissors, they broke, YOU WIN!')
        wins += 1
        print(f'{wins} Wins | {losses} Losses')

    elif Guess == 'p' and PCguess == '1' or PCguess == '5':
        if PCguess == '1':
            print('You suffocated the rock with paper, he is dead, YOU WIN!')
        elif PCguess == '5':
            print('You disprove the spock with your 400 page thesis, YOU WIN!')
        wins += 1
        print(f'{wins} Wins | {losses} Losses')
        
    elif Guess == 's' and PCguess == '4' or PCguess == '2':
        if PCguess == '4':
            print('You snip the lizard in two, why... you win?')
        elif PCguess == '2':
            print('You cut his paper, YOU WIN!')
        wins += 1
        print(f'{wins} Wins | {losses} Losses')

    elif Guess == 'l' and PCguess == '5' or PCguess == '2':
        if PCguess == '5':
            print('Your opponents hand turn purple and begins to swell')
            print('he cries out in pain before he drops to the floor, YOU WIN?')
        elif PCguess == '2':
            print('Your lizard munches on the paper, YOU WIN!')
        wins += 1
        print(f'{wins} Wins | {losses} Losses')

    elif Guess == 'S' and PCguess == '3' or PCguess == '1':
        if PCguess == '3':
            print('You smash his scissors, he cries, YOU WIN!')
        elif PCguess == '1':
            print('Your wipe the opponents rock out of existence along with a few fingers, YOU WIN!')
        wins += 1
        print(f'{wins} Wins | {losses} Losses') 
def isLose():
    if PCguess == 'r' and Guess == '4' or Guess == '3':
        if Guess == '4':
            print('YOU LOSE')
            
        elif Guess == '3':
            print('YOU LOSE')
        losses += 1
        print(f'{wins} Wins | {losses} Losses')

    elif PCguess == 'p' and Guess == '1' or Guess == '5':
        if Guess == '1':
            print('YOU LOSE')
        elif Guess == '5':
            print('YOU LOSE')
        losses += 1
        print(f'{wins} Wins | {losses} Losses')
        
    elif PCguess == 's' and Guess == '4' or Guess == '2':
        if Guess == '4':
            print('YOU LOSE')
        elif Guess == '2':
            print('YOU LOSE')
        losses += 1
        print(f'{wins} Wins | {losses} Losses')

    elif PCguess == 'l' and Guess == '5' or Guess == '2':
        if Guess == '5':
            print('YOU LOSE')
        elif Guess == '2':
            print('YOU LOSE')
        losses += 1
        print(f'{wins} Wins | {losses} Losses')

    elif PCguess == 'S' and Guess == '3' or Guess == '1':
        if Guess == '3':
            print('YOU LOSE')
        elif Guess == '1':
            print('YOU LOSE')
        losses += 1
        print(f'{wins} Wins | {losses} Losses') 

padding()
#load()
print('Start [s] or Quit [q]')
while True:
    start = input('Input: ')
    if start == 'q':
        killGame = True
        print('Game over')
        break
    elif start == 's':
        rules()
        break
    else:
        print('Invalid')

print('')
while killGame == False:
    print(' Rock [r], Paper [p], Scissors [s]')
    print('Lizard [l], Spock [S], see Rules [i]')
    print('            Quit [q]')
    Guess = input('Pick your move: ')
    PCguess = random.randint(1,5)
    # 1 = rock      2 = paper
    # 3 = scissors  4 = lizard
    # 5 = spock
    if Guess == 'i':
        rules()
        print('')
    isWin()
    isLose()
    if Guess == 'q':
        killGame == True
        break

print(f'{wins} wins, {losses} losses')
end = ('Enter anything to close: ')
if type(end) == str:
    exit()
    
