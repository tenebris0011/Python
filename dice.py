#This code is not functional, currently working to resolve looping issues.

import random

min = 0
max = 20

i = random.randint(min,max)

roll = input('Would you like to play a game?')

while roll == "yes":
    print ('''
======================================
You run into a deadly demonic intity.
You must role to save your life.
You must role higher than a 10 to win.
======================================
    ''')
    for i in range(1):
        print (random.randint(min,max))
        if i >= 10:
            print ('''Your staff begins to hum as you say your incantation.
The demonic intitiy, begins to shreak with a blood curtling sound.
You stand your ground, and banish it!''')
        elif i <= 10:
            print ('''You watch in dispair, as the intity devours your friends.
You stand their, with no where to run, knowing that this is the end...''')
if roll == "no":
    print ('Guess you could run too...')
    
