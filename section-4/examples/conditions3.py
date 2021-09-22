#!/usr/bin/env python3

age = int(input("Please enter your age: "))

if age in range(16, 66):
    print("Enjoy your day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Enjoy your day at work")
