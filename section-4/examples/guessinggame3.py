#!/usr/bin/env python

answer = 5
guess = int(input("Please enter a number between 1 and 10: "))

if guess != answer:
    if guess < answer:
        print("Please guess higher.")
    elif guess > answer:
        print("Please guess lower.")

    guess = int(input("Please enter a number between 1 and 10: "))

    if guess != answer:
        print("Sorry, wrong answer.")
    else:
        print("Well done! You guessed correctly this time.")
else:
    print("Well done! You got it first time")
