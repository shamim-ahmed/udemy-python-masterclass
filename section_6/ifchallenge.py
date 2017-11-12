#!/usr/bin/env python

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if (age >= 18) and (age < 31):
    print("Welcome to the holiday, {0} !".format(name))
else:
    print("Sorry {0}, you are not eligible to participate in this holiday".format(name))
    