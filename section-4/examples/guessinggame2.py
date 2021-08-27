#!/usr/bin/env python

answer = 5

guess = int(input("Please enter a number between 1 and 10: "))

if guess < answer:
    print("Please guess higher")
    guess = int(input("Please enter a number between 1 and 10: "))

    if guess == answer:
        print("Well done! You've guessed correctly.")
    else:
        print("Sorry, wrong answer.")
elif guess > answer:
    print("Please guess lower.")
    guess = int(input("Please enter a number between 1 and 10: "))

    if guess == answer:
        print("Well done! You've guessed correctly.")
    else:
        print("Sorry, wrong answer.")
else:
    print("Well done! You've guessed correctly.")
