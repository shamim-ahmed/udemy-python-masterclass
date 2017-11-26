#!/usr/bin/env python

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    
    if guess == 0:
        print("You've chosen to quit. I oblige...")
        break
    
    if guess < answer:
        print("Please guess higher: ")
    elif guess > answer:
        print("Please guess lower: ")
    else:
        print("Congratulations ! You guessed it !") 

