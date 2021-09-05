#!/usr/bin/env python

activity = input("How would you like to spend your time today? ")

# note how caseless comparison is performed
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema!")
