#!/usr/bin/env python3

parrot = "Norwegian Blue"

letter = input("Please enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
