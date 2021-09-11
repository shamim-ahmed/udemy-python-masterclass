#!/usr/bin/env python

import timeit

nested_loop = """\
tlist_1 = []

for i in range(0, 500):
    for j in range(0, 500):
        tlist_1.append((i, j))
"""

result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
print("Nested loop: {}".format(result_1))

list_comp = """\
tlist_2 = [(i, j) for i in range(1, 500) for j in range(1, 500)]
"""

result_2 = timeit.timeit(list_comp, globals=globals(), number=1000)
print("list comprenehsion: {}".format(result_2))
