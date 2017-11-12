#!/usr/bin/env python

parrot = "Norwegian Blue"

c = input("Enter a character: ")

if c in parrot:
    print("The character '{0}' was found in '{1}'".format(c, parrot))
else:
    print("I don't need that letter")
