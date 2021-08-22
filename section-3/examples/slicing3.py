#!/usr/bin/env python

#         01234567890123
parrot = 'Norwegian Blue'

print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Nw
print()

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(ch if ch not in separators else " " for ch in number).split()
print([int(val) for val in values])
