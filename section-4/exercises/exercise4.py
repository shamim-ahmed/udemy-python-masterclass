#!/usr/bin/env python

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age <= 30:
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry {}, you are not eligible".format(name))
