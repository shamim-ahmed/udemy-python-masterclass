#!/usr/bin/env python3

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print()

for i in range(1, a // b):
    print(i)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)
