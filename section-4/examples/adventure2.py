#!/usr/bin/env python3

available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

    if chosen_exit == "quit":
        print("Game over")
        break
else:
    print("Aren't you glad you got out of there?")
