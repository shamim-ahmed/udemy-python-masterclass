#!/usr/bin/env python

import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

nested_loop_sol = """\
for loc in sorted(locations):
    result = []
    for key in exits:
        if loc in exits[key].values():
            result.append((key, locations[key]))

    print("locations leading to {}".format(loc), end="\t")
    print(result)
"""

nested_loop_time = timeit.timeit(nested_loop_sol, globals=globals(), number=5000)

list_comp_sol = """\
for loc in sorted(locations):
    result = [(key, locations[key]) for key in exits if loc in exits[key].values()]
    print("locations leading to {}".format(loc), end="\t")
    print(result)
"""

list_comp_time = timeit.timeit(list_comp_sol, globals=globals(), number=5000)

nested_comp_sol = """\
result = [[(key, locations[key]) for key in exits if loc in exits[key].values()] for loc in sorted(locations)]

for loc, loc_list in enumerate(result):
    print("locations leading to {}".format(loc), end="\t")
    print(loc_list)
"""

nested_comp_time = timeit.timeit(nested_comp_sol, globals=globals(), number=5000)

print(nested_loop_time)
print(list_comp_time)
print(nested_comp_time)
