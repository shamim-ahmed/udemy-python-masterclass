#!/usr/bin/env python3

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy {}".format(item))
