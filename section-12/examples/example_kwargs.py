#!/usr/bin/env python

def print_keyworded_arguments(arg1, **kwargs):
    print("arg1 = {}".format(arg1))

    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


# you can mix keyworded args with non-keyworded args
print_keyworded_arguments("Hello", fruit="Apple", number=10, planet="Jupiter")
