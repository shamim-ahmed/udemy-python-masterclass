#!/usr/bin/env python

meal = ["egg", "bacon", "tomato", "sausages"]

# OMG note the indentation of else block !!!
# also note how nasty_food_item was initialized in else block
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    nasty_food_item = None
    print("I'll have a plate of that, please")

if nasty_food_item:
    print("Can't I have something without spam in it ?")
