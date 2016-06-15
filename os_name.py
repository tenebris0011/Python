import os

name = os.getenv('COMPUTERNAME')

answer = input('Would you like to know your computer\'s name? (yes/no)')

if answer == 'yes':
    print('Your computer\'s name is: ', name)
elif answer == 'no':
    print('Well, maybe some other time than.')
else:
    print('That is not a valid option.')
