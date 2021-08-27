#!/usr/bin/env python

import random

done = False

while done == False:
    answer = random.randrange(1, 11)
    guess = int(input("Please enter a number between 1 and 10: "))

    if guess == answer:
        print("Your guess is correct. The answer is {}".format(answer))
        done = True
    else:
        print("Sorry, your guess was not correct. Please try again")
        print()

print("Have a nice day!")
