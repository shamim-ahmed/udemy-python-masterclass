#/usr/bin/env python

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " World")

greeting = 'Hello'
name = input('Please enter your name: ')
print(greeting + name)
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

# You cannot concatenate an int to a str
# the following line will cause an error if you uncomment it
# print(name + ' is ' + age + ' years old')

# formatting is okay
print("%s is %d years old" % (name, age))

age_in_words = '24 years'
print(name + ' is ' + age_in_words + ' old')

