#!/usr/bin/env python

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

result_1 = [[(burger, topping) for burger in burgers] for topping in toppings]

for index, combinationlist in enumerate(result_1):
    print("list for {}: {}".format(toppings[index], combinationlist))

print("-" * 40)

result_2 = [[(burger, topping) for topping in toppings] for burger in burgers]

for index, combinationlist in enumerate(result_2):
    print("list for {}: {}".format(burgers[index], combinationlist))
