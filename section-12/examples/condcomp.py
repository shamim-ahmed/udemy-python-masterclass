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

result1 = []

for meal in menu:
    if "spam" not in meal:
        result1.append(meal)

print(result1)

# conditional list comprehension
result2 = [meal for meal in menu if "spam" not in meal]
print(result2)

print("-" * 20)

result3 = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(result3)

result4 = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(result4)

print("-" * 20)

result5 = [meal for meal in menu if "spam" in meal or "eggs" in meal if not (
    "bacon" in meal and "sausage" in meal)]
print(result5)

result6 = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not (
    "bacon" in meal and "sausage" in meal)]
print(result6)
