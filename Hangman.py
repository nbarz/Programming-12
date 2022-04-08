import random
import time

# the change I made was the UI

#Hid images in a function to make workspace clear
def image(x):
    picture = {

    '0':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        
    ┃       
    ┃      
    ┃__
    ''',

    '1':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃       
    ┃      
    ┃__
    ''',

    '2':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃        |
    ┃       
    ┃__
    ''',

    '3':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃       /|
    ┃       
    ┃__
    ''',

    '4':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃       /|\\
    ┃       
    ┃__
    ''',

    '5':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃       /|\\
    ┃       / 
    ┃__
    ''',

    '6':'''
    ✚━━━━━━━━-
    ┃        |
    ┃        O
    ┃       /|\\
    ┃       / \\
    ┃__
    '''
    }

    print(picture[x])

#padding between rounds
def padding():
    for v in range(50):
        print('')

words = ['KWANTLEN', 'RAI', 'ZIMMERMAN', 'EXACT', 'SNOW',
'SOUGHT', 'SOMBER', 'CRAVE', 'LENGTH', 'FROZEN', 'MOVIE',
'RETAIL', 'TRAILER', 'DESTROY', 'TINY', 'PHYSICAL', 'FRAGILE',
'DEMOLISH', 'PRAISE', 'ARTICLE', ]

Excluded = ['KWANTLEN', 'RAI', 'ZIMMERMAN']

good = ['nice one.','5 stars','you got one', 'good guess.','you must be cheating.']
bad = ['yikes','what grade are you in... just curious','Hmmm','nope','too bad','not that one','try again',]

#intro
padding()
time.sleep(.5)
print('Loading up...')
time.sleep(1)
print('Tying rope...')
time.sleep(1)
print('Selecting word...')
time.sleep(1.5)

while True:
    #Selects a random word
    #Re-Selects if word is excluded
    word = words[random.randint(0,19)]
    while word in Excluded:
        word = words[random.randint(0,19)]

    #Creates lines to show user how many letters the word is
    #ammount of lines proportional to word length
    wordPublic = []
    for i in word:
        wordPublic.append('_')

    #Variables
    # default values in loop to be able to reset them
    used = []
    GameOver = False
    Lives = 7
    pic = 0
    wincon = 0

    #Showcase of words the player can use
    board = '''
A B C D E F G H I
 J K L M N O P Q
R S T U V W X Y Z

    '''

    while True:

        #Things the player will see
        padding()
        image(str(pic))
        print(f'Lives: {Lives}')
        
        print(' '.join(wordPublic)) #turns list into string ONLY when printed so it is still editable as a list
        print(board)

        guess = input('Guess a letter: ').upper()
        while guess.isalpha() == False:
            print('guess a letter please')
            time.sleep(.2)
            guess = input('Guess a letter: ').upper()
        print('checking...')
        time.sleep(1.5)


        #if the letter isnt used
        if guess not in used:
            if guess not in word:
                board = board.replace(guess, '*')
                pic += 1 #changes the index of hangman stage
                Lives -= 1
                print('')
                print(bad[random.randint(0,5)]) #random lose comment
                time.sleep(1.5)

                if Lives <= 0:
                    print('''
                    ✚━━━━━━━━-  
                    ┃        |
                    ┃        O     You lost
                    ┃       /|\\  He is dead
                    ┃       / \\
                    ┃__
                    ''')
                    choice = input('Quit "q" | Try Again "r" ')
                    while choice.isalpha() == False:
                        print('guess a letter please')
                        time.sleep(.2)
                        choice = input('Quit "q" | Try Again "r" ')
                    if choice == 'q' or choice == 'Q':
                        print('shutting down...')
                        time.sleep(3)
                        exit()
                    elif choice == 'r' or choice == 'R':
                        break

                used.append(guess) # add to bank on used letters
            elif guess in word:

                print('')
                index = word.index(guess) #replace the '_' at a cspecific index to 'leter guessed'
                wordPublic[index] = guess
                used.append(guess)
                print(good[random.randint(0,4)]) #random good comment
                time.sleep(1)

                if ''.join(wordPublic) == word: #if the combination of correct letters == word chosen
                    padding()
                    print (f'wow you got it, the word was {word}')
                    choice = input('Quit "q" | Try Again "r" ')
                    while choice.isalpha() == False:
                        print('guess a letter please')
                        time.sleep(.2)
                        choice = input('Quit "q" | Try Again "r" ')
                    if choice == 'q' or choice == 'Q':
                        print('shutting down...')
                        time.sleep(3)
                        exit()
                    elif choice == 'r' or choice == 'R':
                        break
                    
        else:
            print("You have used this letter already")
            time.sleep(1.5)