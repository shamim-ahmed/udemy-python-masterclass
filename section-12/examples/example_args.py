#!/usr/bin/env python

def print_arguments(arg1, *args):
    print("arg1 = {}".format(arg1))

    for arg in args:
        print(arg)


# pass a variable number of arguments
print_arguments("Hello", 1, 2, 3)
