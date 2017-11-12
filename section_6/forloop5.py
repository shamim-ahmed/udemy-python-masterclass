#!/usr/bin/env python

number = "9,223,372,036,854,775,807"

cleanedNumber = ''

for c in number:
    if c in '0123456789':
        cleanedNumber += c
        
newNumber = int(cleanedNumber)
print("The parsed number is {}".format(newNumber))        
