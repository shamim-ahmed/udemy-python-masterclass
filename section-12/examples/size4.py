#!/usr/bin/env python

import sys

def my_range(n: int):
    val = 0

    while val < n:
        yield val
        val += 1

# create an instance of custom range
big_range = my_range(10000)

# convert the custom range to a list
big_list = list(big_range)

print("The size of big_range is {}".format(sys.getsizeof(big_range)))
print("The size of big_list is {}".format(sys.getsizeof(big_list)))

# try to iterate over the range
# no output will be produced
for x in big_range:
    print(x)
