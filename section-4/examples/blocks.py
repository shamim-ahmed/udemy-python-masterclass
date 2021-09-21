#!/usr/bin/env python3

n = int(input("Please enter a positive integer between 1 and 12: "))

while (n < 0 or n > 12):
    n = int(input("Please enter a positive integer between 1 and 12: "))

for i in range(1, n + 1):
    print("No. {:2} squard is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)
