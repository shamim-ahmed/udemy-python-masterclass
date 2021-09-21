#!/usr/bin/env python3

numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All the numbers are fine")
