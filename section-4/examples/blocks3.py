#!/usr/bin/env python3

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("You are eligible to vote")
    print("Please put an X in the box")
