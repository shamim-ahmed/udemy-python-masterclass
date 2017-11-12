#!/usr/bin/env python

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("The parrot is " + state)

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2:3}".format(j, i, i * j), end = '\t')
    
    print()
