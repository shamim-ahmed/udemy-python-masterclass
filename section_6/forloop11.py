#!/usr/bin/env python

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = None

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
    else:
        print("I'll have a plate of {}, please".format(item))

if nasty_food_item:
    print("Can't I have something without spam in it ?")
