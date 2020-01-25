#!/usr/bin/env python

digit_str = "1234567890"
my_iterator = iter(digit_str)

for i in range(0, len(digit_str)):
    print(next(my_iterator))
