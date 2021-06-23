import time
import random
import string
import os
os.system('cls')

chars = string.ascii_lowercase + string.ascii_uppercase + '!@#$'


while True:
    length = input('length of password: ')

    if length.lower() == 'q':
        exit()

    try:
        length = int(length)
    except:
        print('enter a valid number')
        continue
    
    try:
        if length < 6:
            print('enter a number longer than 6')
            continue
        else:
            chars_choice = "".join(random.choice(chars) for i in range(1,length+1))
            print(chars_choice)
            continue
    except:
        continue