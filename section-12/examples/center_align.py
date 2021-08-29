#!/usr/bin/env python

result = ["fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(1, 31)]

# note how the output is center aligned
for s in result:
    print(s.center(12, " "))
