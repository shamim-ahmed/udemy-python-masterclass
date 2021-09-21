#!/usr/bin/env python

choice = None

while choice != '0':
    choice = input("Please enter your choice. Press Enter to exit: ")

    if choice == '':
        break
else:
    print("Bye bye")
