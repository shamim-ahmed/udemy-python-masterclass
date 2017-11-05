#!/usr/bin/env python

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher: ")
    guess = int(input())
    if guess == 5:
        print("Congratulations ! You guessed it !")
    else:
        print("Sorry, your guess was incorrect")
elif guess > 5:
    print("Please guess lower: ")
    guess = int(input())
    if guess == 5:
        print("Congratulations ! You guessed it !")
    else:
        print("Sorry, your guess was incorrect")#
else:
    print("You got it first time !!!")
