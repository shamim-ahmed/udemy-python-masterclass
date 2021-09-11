#!/usr/bin/env python

import random

highest = 10
answer = random.randint(1, highest)

is_done = False

while not is_done:
    # obtain user input
    guess = int(input("Please enter a number between 1 and {}: ".format(highest)))

    if guess == answer:
        is_done = True
        print("Well done! The correct answer is {}".format(answer))
    else:
        suggestion = "Please guess higher" if guess < answer else "Please guess lower"
        print(f"Sorry, your guess is incorrect. {suggestion}")
