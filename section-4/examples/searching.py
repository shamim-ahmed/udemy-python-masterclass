#!/usr/bin/env python

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
item_index = None

if item_to_find in shopping_list:
    item_index = shopping_list.index(item_to_find)

if item_index != None:
    print("{} found at index {}".format(item_to_find, item_index))
else:
    print("{} not found".format(item_to_find))
