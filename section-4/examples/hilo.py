#!/usr/bin/env python3

low = 1
high = 1000

print("Guess a number between {} and {}".format(low, high))
input("Press ENTER to start")

count = 1

while True:
    guess = low + (high - low) // 2
    print("My guess is {}. Should I guess higher or lower?".format(guess))
    suggestion = ""

    while suggestion not in ["l", "h", "c"]:
        suggestion = input("Please enter h or l, or c if my guess is correct: ")

    if suggestion == "c":
        print("I got it in {} guesses".format(count))
        break

    if suggestion == "l":
        high = guess - 1
    elif suggestion == "h":
        low = guess + 1 
    
    count += 1
