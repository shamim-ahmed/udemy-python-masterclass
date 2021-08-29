#!/usr/bin/env python

# declare a list of numbers
numbers = list(range(1, 7))
number = 0

while True:
    number = int(input("Please enter a number between 1 and 6: "))

    if 1 <= number <= 6:
        break

# Note that the variable used in list comprehension has the same name as that of a local variable
# However, this does not change the value of the local variable
squares = [number ** 2 for number in numbers]

idx = numbers.index(number)
result = squares[idx]
print("The square value is: {}".format(result))
