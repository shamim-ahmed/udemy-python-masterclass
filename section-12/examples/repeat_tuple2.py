#!/usr/bin/env python

from itertools import repeat

my_tuple = (1, 3)

result = tuple(repeat(my_tuple, 4))

print(result)
