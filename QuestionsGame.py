from ast import If
from pickle import TRUE
import time

active = True
score = 0
#change questions here
Questions = {
    'q1':'How many chromosomes does a human have? ', 
    'q2':'What does ATM stand for? ', 
    'q3':'What version of Windows did Microsoft skip? ', 
    'q4':'What movie character famously says "Ill be back" ', 
    'q5':'What is the name of our galaxy? ', 
    'q6':'Is an electron have a positive or negative charge? ', 
    'q7':'How many cents in a dollar? ', 
    'q8':'What is 100m/s in km/h? ', 
    'q9':'How many days are in a year? ', 
    'q10':'How many seconds are in a day? ', 
}
#change answers here
Answers = {
    'a1':'46', 
    'a2':'automated teller machine', 
    'a3':'9', 
    'a4':'the terminator', 
    'a5':'the milky way', 
    'a6':'negative', 
    'a7':'100', 
    'a8':'360', 
    'a9':'365', 
    'a10':'86400', 
}
def padding():
    for i in range(5):
        print("\n")
#ask question and  wait for answer
def ask(question,answer):
    padding()
    guess = input(Questions[question])
    if guess.isnumeric() == True:
        if guess == Answers[answer]:
            print('correct!')
            return 1
        else:
            print('incorrect!')
            return 0
    else:
        if guess.lower() == Answers[answer]:
            print('correct!')
            return 1
        else:
            print('incorrect!')
            return 0

time.sleep(.5)
print('Welcome to Crazy Questionair')
time.sleep(.5)
print('Lets get started')
time.sleep(1)

while active == True:
    #updates score depending on value returned
    #value returned depends on being right or wrong
    score += ask('q1','a1')
    score += ask('q2','a2')
    score += ask('q3','a3')
    score += ask('q4','a4')
    score += ask('q5','a5')
    score += ask('q6','a6')
    score += ask('q7','a7')
    score += ask('q8','a8')
    score += ask('q9','a9')
    score += ask('q10','a10')


    print(f'you got {score * 10}% of the question right')
    if (score * 10) < 50: #if they got less tahn 50%
        print('Better luck next time')
    else:
        print('Nice job')
    while True:
        choice = input('restart |r| or quit |q|')
        if choice == 'r':
            break
        elif choice == 'q':
            active = False
            break
        else:
            print('invalid response')

print('closing...')
time.sleep(1.5)