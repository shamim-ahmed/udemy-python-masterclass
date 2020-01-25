#!/usr/bin/env python

list_1 = []
list_2 = list()

print("list_1 = {}".format(list_1))
print("list_2 = {}".format(list_2))

if list_1 == list_2:
    print("two lists are identical")

list_3 = list("This is a test")

for item in list_3:
    print(item)
