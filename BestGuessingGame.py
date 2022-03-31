from importlib.metadata import version
import random
import time


def shutdown():
    print('shutting down.')
    time.sleep(.5)
    print('shutting down..')
    time.sleep(.5)
    print('shutting down...')
    time.sleep(.5)
    
def buffer(): 
    print(' ')
    print(' ')
    print(' ')
    print(' ')

def starter():
    print('')
    print('Booting up.')
    time.sleep(0.5)
    print('Booting up..')
    time.sleep(0.5)
    print('Booting up...')
    time.sleep(0.5)
    print('')

Guess = 0
high = 100
low = 1
count = 1
activeGame = True
hardReset = True
off = False

def reset():
    print('Restarting.')
    time.sleep(.5)
    print('Restarting..')
    time.sleep(.5)
    print('Restarting...')

while hardReset == True and off == False:
    Guess = 0
    high = 100
    low = 1
    count = 1
    activeGame = True
    hardReset = True
    off = False
    buffer()
    print('version 1: computer guesses your number')
    print('version 2: you guess the computers number')
    while True :
        Version = input('Game 1 or Game 2:  ')
        #using the int(input()) stops the code if a string is entered
        if Version.isnumeric() == True: #prevents non number inputs
            Version = int(Version) 
            if Version == 1:
                print('')
                print('Version 1 selected')
                print('')
                activeGame = True
                break
            elif Version == 2:
                print('')
                print('version 2 selected')
                print('')
                activeGame = True
                break
        print("that Version is in development")

    while activeGame == True:
        if Version == 1 and activeGame == True:
            starter()
            while True:
                Ans = input('Select a number from 1 - 100: ')
                if Ans.isnumeric() == True: #Checks if string input has ONLY numbers
                    Ans = int(Ans) # if it has only numbers it is turned into an integer
                    #using the int(input()) stops the code if a string is entered
                    if type(Ans) == int and Ans <= 100 and Ans >= 1:
                        print(f'the magic number is {Ans}')
                        break
                
                print('Invalid input')
            
            Guess = 0
            count = 1
            while Guess != Ans:
                print('')
                print('Mr.Computer is thinking')
                time.sleep(1)
                Guess = random.randint(low, high)
                print(f'computer answered {Guess}')
                count += 1
                print('')

                if Guess == Ans:
                    time.sleep(1)
                    print(f'Mr.Computer guessed it in {count} tries')
                    break

                while True:
                    print('print "H" (higher) or "L" (lower) to give him a hint')
                    difference = input('Hint: ')
                    if difference == "H":
                        low = Guess + 1
                        break
                    elif difference == "L":
                        high = Guess - 1
                        break
                    else:
                        print('its rude not to give hints')
                        print('')
            while True:  
                nextPath = input('Would you like to Quit (q), Restart (r) or Change versions (c): ')
                print('')
                if nextPath == "q":
                    shutdown()
                    activeGame = False
                    off = True
                    break
                elif nextPath == 'r':
                    reset()
                    break
                elif('c'):
                    reset()
                    activeGame = False
                    break

                else:
                    print('invalid input')

        if Version == 2 and activeGame == True:
            starter()
            Ans = random.randint(1,100)
            print('magic number has been generated!!')

            while True:
                Guess = input(f'Guess a number from {low} - {high}: ')
                if Guess.isnumeric() == True:
                    Guess = int(Guess)
                    if Guess < Ans:
                        low = Guess + 1
                        print('Too low, guess higher')
                        print('')
                        count += 1
                    elif Guess > Ans:
                        high = Guess - 1
                        print('Too high, guess lower')
                        print('')
                        count += 1
                    elif Guess == Ans:
                        print(f'WOW, you got it in {count} tries!!')
                        break
                else:
                    print('Invalid guess')
                    print('')
            # restart or quit sequence
            while True:  
                nextPath = input('Would you like to Quit (q), Restart (r) or Change versions (c): ')
                print('')
                if nextPath == "q":
                    shutdown()
                    activeGame = False
                    off = True
                    break
                elif nextPath == 'r':
                    reset()
                    break
                elif('c'):
                    reset()
                    activeGame = False
                    break

                else:
                    print('invalid input')

print('')
print('Goodbye')
buffer()

