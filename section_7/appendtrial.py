#!/usr/bin/env python

parrot_list = ["Not pinin'", "No more", "A stiff", "Bereft of life"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is {}".format(state))
    
even_list = [2, 4, 6, 8]
odd_list = [1, 3, 5, 7, 9]

number_list = even_list + odd_list
number_list.sort()
print(number_list)
