#!/usr/bin/env python

import sys

big_range = range(10000)
big_list = list(big_range)

print("The size of big range is {} byes".format(sys.getsizeof(big_range)))
print("The size of big list is {} byes".format(sys.getsizeof(big_list)))
