#!/usr/bin/env python3

low = 1
high = 1000

print("Guess a number between {} and {}".format(low, high))
input("Press ENTER to start")

count = 1
guess = None
done_flag = False

while not done_flag:
    guess = low + (high - low) // 2
    print("My guess is {}. Should I guess higher or lower?".format(guess))
    suggestion = ""

    while suggestion not in ["l", "h", "c"]:
        suggestion = input("Please enter h or l, or c if my guess is correct: ")

    if suggestion == "l":
        high = guess - 1
        count += 1
    elif suggestion == "h":
        low = guess + 1 
        count += 1
    else:
        print("I got it in {} guesses".format(count))
        done_flag = True
else:
    print("You thought of the number {}".format(guess))
    print("I got it in {} guesses".format(count))
