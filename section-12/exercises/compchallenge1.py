#!/usr/bin/env python

# Create a new Python file - I've called this one "fizzbuzz.py".
#
# Use the conditional expression from the previous video to produce
# a list comprehension that returns the fizzbuzz results.
#
# If a number's divisible by 3, the value should be "fizz".
# If it's divisible by 5, the value should be "buzz".
# If it's divisible by both 3 and 5, the value should be "fizz buzz"
# Finally, if none of those conditions apply, the value will be the number itself.
#
# The code from the end of the last video appears below, so you can check the result.

result = ["fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(1, 31)]
print(result)    
