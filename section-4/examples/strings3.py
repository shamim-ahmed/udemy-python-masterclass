#!/usr/bin/env python

number = "9,223;372:036 854,775;807"
separators = ""

for c in number:
    if not c.isnumeric():
        separators += c

print(separators)

values = "".join([c if c not in separators else " " for c in number]).split()

print([int(val) for val in values])
