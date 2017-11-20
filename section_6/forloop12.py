#!/usr/bin/env python

number = "9,223,372,036,854,775,807"
cleanedNumber = ""

for c in number:
    if c == ',':
        continue
    
    cleanedNumber += c
    
newNumber = int(cleanedNumber)
print("The number is {0}".format(newNumber))

x = 23
x += 2
print(x)

x -= 5
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

