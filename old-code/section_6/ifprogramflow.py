#!/usr/bin/env python

name = input("What is your name ? ")
age = int(input("How old are you, {0} ? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote !")
    print("Please put an X in the ballot box")
else:
    print("Please come back after {0} years".format(18 - age))
