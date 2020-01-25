#!/usr/bin/env python

age = int(input("Please enter your age: "))

if not(age < 18):
    print("You are old enough to vote")
    print("Please put an X in the right box")
else:
    print("Please come back in {0} years".format(18 - age))
