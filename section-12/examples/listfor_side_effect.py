#!/usr/bin/env python

numbers = list(range(1, 7))
squares = []
number = 0

while True:
    number = int(input("Please enter a number between 1 and 6: "))

    if 1 <= number <= 6:
        break

# BUG ALERT: the name of the loop variable is the same as that of a local variable
for number in numbers:
    squares.append(number ** 2)

# At this point, the value of number is 6
idx = numbers.index(number)
result = squares[idx]
print("The square value is: {}".format(result))
