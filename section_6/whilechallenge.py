#!/usr/bin/env python

import random

highest = 10
answer = random.randint(1, highest)
guess = int(input("Please guess a number between 1 and {}: ".format(highest)))

if guess != answer:
    done = False
    
    while not done:
        if guess == 0:
            print("You chose to quit. I oblige...")
            done = True
        elif guess == answer:
            print("Congratulations ! You guessed it !")
            done = True
        elif guess < answer:
            guess = int(input("Please guess higher: "))
        else:
            guess = int(input("Please guess lower: "))
            
else:
    print("Wow ! You guessed it FIRST TIME !")
