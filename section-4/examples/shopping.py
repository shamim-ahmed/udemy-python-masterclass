#!/usr/bin/env python

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy {}".format(item))
