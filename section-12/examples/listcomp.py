#!/usr/bin/env python

# print the aboslute path of the current file
print(__file__)

# declare a list of numbers
numbers = list(range(1, 7))

# use list comprehension to get a list of squares
squares = [n ** 2 for n in numbers]

print(squares)
