#!/usr/bin/env python

number = "9,223;372:036 854,775;807"
separators = number[1::4]

print(separators)

values = "".join([c if c not in separators else " " for c in number])
print(values)
