#!/usr/bin/env python

#         01234567890123
parrot = 'Norwegian Blue'

print(parrot[0:6])    # Norweg
print(parrot[-14:-8])
print()

print(parrot[3:6])    # weg
print(parrot[-11:-8])
print()

print(parrot[0:9])    # Norwegian
print(parrot[-14:-5])
print()

print(parrot[:9])     # Norwegian
print(parrot[:-5])
print()

print(parrot[10:14])  # Blue
print(parrot[-4:])
print()

print(parrot[:6])     # Norweg
print(parrot[:-8])
print()

print(parrot[6:])     # ian Blue
print(parrot[-8:])
print()

print(parrot[:6] + parrot[6:])    # Norwegian Blue
print(parrot[:-8] + parrot[-8:])
print()

print(parrot[:])
