#!/usr/bin/env python

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["fish", "pizza", "cheese"])
menu.append(["spam", "rice", "curry"])

for dish in menu:
    if "spam" not in dish:
        for item in dish:
            print(item)
        print()
