#!/usr/bin/env python

import random

highest = 10
answer = random.randint(1, highest)

guess = int(input("Please guess a number between 1 and {}: ".format(highest)))

if guess != answer:
    if guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess lower: ")
        
    guess = int(input())
    
    if guess == answer:
        print("Congratulations! You guessed it !")
    else:
        print("Sorry, your guess was not correct")
else:
    print("Wow! You guessed it FIRST TIME !")
 