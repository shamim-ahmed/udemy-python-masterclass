#!/usr/bin/env python

parrot = "Norwegian Blue"

letter = input("Please enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
