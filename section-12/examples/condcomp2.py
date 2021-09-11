#!/usr/bin/env python

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

items = set()

for meal in menu:
    for item in meal:
        items.add(item)

for meal in menu:
    for item in items:
        if item in meal:
            print("{} is in {}".format(item, meal))
    print("-" * 20)
