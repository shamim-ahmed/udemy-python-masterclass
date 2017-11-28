# /usr/bin/env python

even_list = [2, 4, 6, 8]
another_even_list = list(even_list)

print("Are two lists equal ? : {}".format(even_list == another_even_list))

another_even_list.sort(reverse=True)
print("Are two lists equal ? : {}".format(even_list == another_even_list))
print(another_even_list)
