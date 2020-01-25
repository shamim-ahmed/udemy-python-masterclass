# /usr/bin/env python

even_list = [2, 4, 6, 8]
odd_list = [1, 3, 5, 7, 9]

number_list = [even_list, odd_list]
print(number_list)

for item in number_list:
    print(item)
    
    for n in item:
        print(n)
        
    print()
