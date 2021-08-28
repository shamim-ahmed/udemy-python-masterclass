#!/usr/bin/env python

import sys

def my_range(n: int):
    val = 0

    while val < n:
        yield val
        val += 1

big_range = my_range(10000)
print("The size of big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []

for x in big_range:
    big_list.append(x)

print("The size of big_list is {} bytes".format(sys.getsizeof(big_list)))
