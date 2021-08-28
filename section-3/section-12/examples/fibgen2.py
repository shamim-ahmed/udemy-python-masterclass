#!/usr/bin/env python

# define fibonacci number generator
def fibonacci():
    x, y = 0, 1

    while True:
        yield x
        x, y = y, x + y

# create fibonacci generator
fib = fibonacci()

for i in range(20):
    print(next(fib))
