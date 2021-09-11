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

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contins egg")

print()

items = set()

for meal in menu:
    for item in meal:
        items.add(item)

print(items)
print()

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

result1 = []

for meal in menu:
    if "spam" not in meal:
        result1.append(meal)
    else:
        print("A meal was skipped")

print(result1)
print()

result2 = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(result2)
print()

result3 = [meal for meal in menu if "spam" in meal or "egg" in meal if not "bacon" in meal and "sausage" in meal]
print(result3)
print()

result4 = [meal for meal in menu if ("spam" in meal or "egg" in meal) and ("bacon" not in meal and "sausage" in meal)]
print(result4)
print()

