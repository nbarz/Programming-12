from PIL import Image
import time
quest = 0

def space_line(x):
    time.sleep(x)
    print('\n')

def lose():
    y = Image.open("End.png")
    y.show()
    print('You lose')
    time.sleep(.5)
    print('Closing...')
    time.sleep(2)
    exit()

def intro():
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
    time.sleep(1)
    print('Loading 93%')
    time.sleep(.7)
    print('Loading 100%')
    time.sleep(1)
    print('')
    print('Done!')
    time.sleep(2)
    for i in range(50):
        print('\n')

def padding():
    for i in range(50):
        print("\n")









#intro()

print('''

▀█▀ █▀▀ ▀▄▀ ▀█▀   ▄▀█ █▀▄ █░█ █▀▀ █▄░█ ▀█▀ █░█ █▀█ █▀▀
░█░ ██▄ █░█ ░█░   █▀█ █▄▀ ▀▄▀ ██▄ █░▀█ ░█░ █▄█ █▀▄ ██▄
''')
menu = input('               PRESS |ENTER| TO START')
padding()


#choosing a valid name
while True:
    print('What is your name young adventurer?')
    name = input('name: ')
    while name.isalpha() == False: #check for non letters
        print('''
Thats a bit hard to pronounce,
is there another name you go by?
        ''')
        name = input('name: ')
    while True:
        print(f'so your name is {name}, correct?') #name confirmation
        confirm = input('|Y| or |N| :')
        if confirm.lower() == 'y' or confirm.lower() == 'n': #valid input?
            break
        else:
            print('\n')
            print('are you gonna give me an answer')
            print('\n')
            time.sleep(1)
    
    if confirm.lower() == 'y':
        print('\n')
        print(f'{name} is a mighty name adventurer')
        print('\n')
        time.sleep(1)
        break
    if confirm.lower() == 'n':
        print('\n')
        print('oh..')
        continue

print('''
Welcome to the Adventurers Guild!!
 ______________________________
 |      Adventurers Card      |
 |  |    |       lv 1         |
 |  \\/<>\\/       HP 1         |
 |   |^^|        MP 10        |
 |   |  |        FP 10        |
 |____________________________|

''')

print('start your adventure?')
choice = input('|Y| or |N| ')
if choice.lower() == 'y':
    padding()

elif choice.lower() == 'n':
    print("\n")
    print('You lacked ambition so you were kick out')
    print('failed before you even started')
    time.sleep(3)
    print("\n")
    loser = input('press |ENTER| to do the walk of shame')
    exit()

else:
    print("\n")
    print('your intelect was far to low, even for a lv.1')
    print('you were kicked out because you cant follow instructions')
    time.sleep(3)
    print("\n")
    loser = input('press |ENTER| to work at the mines instead')
    exit()


b = "Studying map" + ".     15%"
print (b, end="\r")
time.sleep(1.5)

b = "Studying map" + ".     30%"
print (b, end="\r")
time.sleep(1)

b = "Packing bag." + ".     55%"
print (b, end="\r")
time.sleep(1.5)

b = "Packing bag." + ".     70%"
print (b, end="\r")
time.sleep(.5)

b = "Tying shoelaces.." + ". 90%"
print (b, end="\r")
time.sleep(1.5)

b = "Tying shoelaces.." + ".100%"
print (b, end="\r")
time.sleep(1.5)
padding()

print('You enter the guild to choose your first quest!')
space_line(2)
print('You scan the chaotic quest board, eager to prove yourself.')
space_line(2)
print('You settle on three quests.')
print('|Goblin Hunting|  |Parcel Delivery| |Dragon Hunting|')
while True:
    choice = input('|1| |2| |3| ')
    if choice == '1':
        quest = choice
        break
    elif choice == '2':
        quest = choice
        break
    elif choice == '3':
        quest = choice
        break
    else:
        print("\n")
        print('The quest board is crowded, better choose from what we have')
        space_line(.5)


if quest == '3':
    padding()
    print('For months you have marched to reach the base of Dragon Scale Mountain')
    space_line(1.5)

    x = Image.open("Q3 mountain.jpg")
    x.show()

    print('\n')
    print('|Set up camp| or |start the acent|?')
    print('\n')
    while True:
        choice = input('|1| or |2|')
        if choice == '1':
            time.sleep(1)
            print('The sun falls in the distance while the stars reveal themselves...')
            space_line(2)
            print('''You rest your weary eyes, fatigued from your journey.
As you drift in to sweet slumber you dream of what awaits atop the mountains peek.''')
            space_line(2)
            print('''Perhaps you slept Too well, you heart stops in your sleep;
I guess most people die at thirty anyway.''')
            print('\n')
            lose()

        elif choice == '2':
            time.sleep(1)
            print('You press on, inspired by vast mountain range...')
            space_line(2)
            print('''You begin your acent and you can feel your heart fluttering with excitement''')
            space_line(2)
            print('''Your so excited the futtering doesnt stop... in fact it becomes faster''')
            space_line(2)
            print('''You clutch your chest as your heart stalls and drop to your knees''')
            space_line(2)
            print('''Maybe resting before the acent would have been better''')
            space_line(2)
            lose()
        else:
            time.sleep(.5)
            print('the surrounding forest is dense, we dont have many options.')
            time.sleep(.5)

if quest == '2':
    padding()
    print('Your step out of the guild hall with a package you must deliver')
    space_line(2)
    print('You decide to waste no time and deliver it as quickly as possible')
    space_line(2)
    print('''The thieves also decided to waste no time and swipe the package out of you hands
as quickly as possible''')
    space_line(3)
    print('You give chase and see him round a corner')
    space_line(2)
    print('|Run faster| or take a left and |cut him off|')
    choice = input('|1| or |2| ')
    while True:
        if choice == '1':
            print('you run even faster and round the same corner')
            space_line(2)
            print('you begin to gain on the thief')
            space_line(2)
            break
        elif choice == '2':
            print('your leather boots slide on the course dirt road and your swerve into an alley')
            space_line(2)
            print('bobbing and weaving through cargo and people you shoot out the other side and block the thief')
            space_line(2)
            print('he grinds to a halt and take of in the other direction')
            space_line(2)
            break
        else:
            print('the towns layout limits your options')
            time.sleep(.5)
            choice = input('|1| or |2|')
    print('You gain on the thief')
    space_line(2)
    print('they whistle sharply as if to signal for something')
    space_line(2)
    print('Two large men leap out of alley ways on each side')
    space_line(2)
    print('they crush you beneth their weight')
    space_line(2)
    lose()

if quest == '1':
    padding()

    print('You follow the main road on your way to the Eastern forest')
    space_line(2)
    print('''you seen a man shrouded in mangled leather gear walking the opposite direction as you
perhaps a trader or fellow adventurer''')
    space_line(2)

    print('You contemplate |crossing the road| or |continuing forward|')
    choice == input('|1| or |2|')
    while True:
        if choice == '1':
            print('You begin to run across the main road')
            space_line(2)
            print('the man calls out to you and you tuen to face him, but you can make out what hes yelling')
            space_line(2)
            print('suddenly you feel a sudden impact against your back')
            space_line(2)
            print('''You crossed the road without looking and you were hit by a carriage and your
body was crushed beneth the hoofs of several war horses''')
            space_line(2)
            print('the stranger helps the driver toss you mangled bandy into the forest to feed the plants')
            space_line(2)
            lose()
        elif choice == '2':
            print('You give it little thought and you continue forward')
            space_line(2)
            print('You hear a carriage comming behind you so you stick to the side of the road')
            space_line(2)
            print('you bump the shoulder of the stranger as the carriage passes')
            space_line(2)
            print('without warning he grabs your wrist and pulls out a knife')
            space_line(2)
            print('you are stabbed 17 times before he spits on your soon to be dead body')
            space_line(2)
            print('''Reports say we was the wanted leader of a group of bandits, luckily the discovery of your
body led authorities to believe he was in the nearby town and was haistily arrested.''')
            space_line(2)
            lose()
        else:
            print('Your mind is focused on the options you already came up with')
            time.sleep(.5)
            choice == input('|1| or |2|')

