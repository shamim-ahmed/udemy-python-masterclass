#!/usr/bin/env python

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = None

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't I have something without spam in it ?")