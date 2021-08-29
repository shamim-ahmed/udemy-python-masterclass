#!/usr/bin/env python

# print the absolute path of the current file
print(__file__)

numbers = list(range(1, 7))
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)
