import random
min = 0
max = 20

roll = input('Would you like to play a game? ')

print (roll)

while roll == 'yes' or roll == "y":
    print ('''
======================================
You run into a deadly demonic intity.
You must role to save your life.
You must role higher than a 10 to win.
======================================
    ''')
    dice_value=(random.randint(min,max))
    print ("You Rolled " + str(dice_value))

    if dice_value >= 11:
      print ('''Your staff begins to hum as you say your incantation.
The demonic intitiy, begins to shreak with a blood curtling sound.
You stand your ground, and banish it!''')
    elif dice_value <= 11:
      print ('''You watch in dispair, as the intity devours your friends.
You stand their, with no where to run, knowing that this is the end...''')
    roll=input('Roll Again?')
if roll == "no" or roll == "n":
  print ('Guess you could run too...')
