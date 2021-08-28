#!/usr/bin/env python

# define generator for odd numbers
def oddnumbers():
    n = 1

    while True:
        yield n
        n += 2

# define generator for pi
def pi_series():
    odds = oddnumbers()
    approximation = 0

    while True:
        approximation += 4 / next(odds)
        yield approximation
        approximation -= 4 / next(odds)
        yield approximation

# generate approximate values of pi
approx_pi = pi_series()

for i in range(1000):
    print(next(approx_pi))
