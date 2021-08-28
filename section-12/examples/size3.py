#!/usr/bin/env python

import sys

# use built-in range
big_range = range(10000)

# note how range is converted to a list
big_list = list(big_range)

print("The size of big range is {} byes".format(sys.getsizeof(big_range)))
print("The size of big list is {} byes".format(sys.getsizeof(big_list)))
