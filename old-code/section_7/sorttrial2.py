#!/usr/bin/env python

even_list = [2, 4, 6, 8]
odd_list = [1, 3, 5, 7, 9]

number_list = even_list + odd_list
sorted_number_list = sorted(number_list)

print(sorted_number_list)

if number_list == sorted_number_list:
    print("Two lists are equal")
else:
    print("Two lists are not equal")
