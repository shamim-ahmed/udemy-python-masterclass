#!/usr/bin/env python

dish = ["fish", "kebab", "curry", "biriyani", "salad"]
my_iterator = iter(dish)

for i in range(0, len(dish)):
    print(next(my_iterator))
