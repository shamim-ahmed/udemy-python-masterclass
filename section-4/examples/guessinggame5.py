#!/usr/bin/env python

import random

highest = 10
# randint returns a number from the provided range, including both endpoints 
answer = random.randint(1, highest)

# obtain user input
guess = int(input("Please enter a number between 1 and {}: ".format(highest)))

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")        
    else:
        print("Please guess lower")

    guess = int(input("Please enter a number between 1 and {}: ".format(highest)))

    if guess == answer:
        print("Well done! You have guessed correctly")
    else:
        print("Sorry, you have not guessed correctly")
