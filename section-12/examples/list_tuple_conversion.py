#!/usr/bin/env python

# declare the tuple
values = (1, 2, 3, 4, 5)

# convert the tuple to a list
values_list = list(values)

# produce a tuple containing the square of each value in the list
result = tuple([x ** 2 for x in values_list])

print(result)
