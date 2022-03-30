import random
import time

killGame = False


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
print('')
print('WELCOME TO MADLIBS v1.07a')

while killGame == False:
    
#Game type selector
    print('SELECT A VERSION| [1] [2] [3] |OR QUIT| [q] |')
    while True:
        version = input('version: ')
        if version == '1' or version == '2' or version == '3':
            print(f'version {version} selected')

        elif version == 'q' or version == 'Q':
            killGame = True

        else:
            print('invalid')
            continue

        break

#inputs for blanks
    print('')

    noun = input('enter a noun: ')
    adjective = input('enter an adjective: ')
    Pnoun = input('enter a plural noun: ')
    limb = input('enter a body part: ')
    num = input('enter a number: ')
    place = input('enter a place: ')
    ing = input('enter a verb (action word) that ends with "ing": ')

    print('')
    print('compiling.')
    time.sleep(.2)
    print('compiling..')
    time.sleep(.2)
    print('compiling...')
    time.sleep(.2)
    print('')

    if version == '1':
        print(f'''
        Once upon a time there was a {adjective} {noun}. Such a valuable object was carried by a man who owned many {Pnoun}
        in a dimensional storage pouch around their {limb}. Legends say he carried it for {num} days and {num}
        nights, always {ing}. They say he now resides in {place}.
        ''')
    if version == '2':
        print(f"""
        In the beggining there was a {noun}, and it was very {adjective}. several {Pnoun} orbited it.
        From the {noun} sprouted {num} {limb}s. They began to create a city by {ing}, it was named {place}.
        """)
    if version == '3':
        print(f"""
        There was a {noun} and a {limb}, they were both {adjective}. they lived in {place} and had many {Pnoun}.
        Last I checked they had around {num}. {ing} was their favourite activity.
        """)

    print('')
    ending = input('Restart [r] or quit [q] : ')

    if ending == 'q':
        KillGame = True
        break
print('')
print('Bye Bye')
time.sleep(.5)
print('Thanks for playing')