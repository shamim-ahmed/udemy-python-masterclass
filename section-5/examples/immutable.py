#!/usr/bin/env python3

result = "Correct"
another_result = result

print(id(result))
print(id(another_result))
print()

result += "ish"

print(id(result))
print(id(another_result))
