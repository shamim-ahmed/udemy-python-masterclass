#!/usr/bin/env python

for i in range(1, 31):
    fizzbuzz = "fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i)
    print(fizzbuzz)
