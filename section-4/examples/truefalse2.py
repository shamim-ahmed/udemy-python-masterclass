#!/usr/bin/env python

# test with nonzero value
answer = 5

if answer:
    print("True")
else:
    print("false")

# test with zero value
answer = 0

if answer:
    print("True")
else:
    print("False")

print("-" * 20)

# test with non empty list
fruits = ["apple"]

if fruits:
    print("True")
else:
    print("False")

# test with empty list
fruits.pop()

if fruits:
    print("True")
else:
    print("false")

print("-" * 20)

# test with non-empty range
myRange = range(5)

if myRange:
    print("True")
else:
    print("false")

# test with empty range
myRange = range(0)

if myRange:
    print("True")
else:
    print("false")
