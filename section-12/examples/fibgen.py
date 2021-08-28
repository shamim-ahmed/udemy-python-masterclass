#!/usr/bin/env python

# define fibonacci number generator
def fibonacci():
    x = 0
    y = 1

    while True:
        yield x
        z = x + y
        x = y
        y = z

# create fibonacci generator
fib = fibonacci()

for i in range(20):
    print(next(fib))
