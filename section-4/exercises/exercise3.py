#!/usr/bin/env python3

answer = 5
guess = int(input("Please enter a number between 1 and 10: "))

if guess == answer:
    print("Well done! You got it first time")
else:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower.")

    guess = int(input("Please enter a number between 1 and 10: "))

    if guess != answer:
        print("Sorry, wrong answer.")
    else:
        print("Well done! You guessed correctly this time.")
