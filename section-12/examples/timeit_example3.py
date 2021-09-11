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


def nested_loop():
    for loc in sorted(locations):
        result = []
        for key in exits:
            if loc in exits[key].values():
                result.append((key, locations[key]))

        print("locations leading to {}".format(loc), end="\t")
        print(result)


def list_comprehension():
    for loc in sorted(locations):
        result = [(key, locations[key])
                  for key in exits if loc in exits[key].values()]
        print("locations leading to {}".format(loc), end="\t")
        print(result)


def nested_comprenehsion():
    result = [[(key, locations[key]) for key in exits if loc in exits[key].values()]
              for loc in sorted(locations)]

    for loc, loc_list in enumerate(result):
        print("locations leading to {}".format(loc), end="\t")
        print(loc_list)


if __name__ == "__main__":
    nested_loop_time = timeit.timeit(
        nested_loop, globals=globals(), number=5000)
    print("nested loop: {}".format(nested_loop_time))
    print("-" * 50)

    list_comp_time = timeit.timeit(
        list_comprehension, globals=globals(), number=5000)
    print("list comprehension: {}".format(list_comp_time))
    print("-" * 50)

    nested_comp_time = timeit.timeit(
        nested_comprenehsion, globals=globals(), number=5000)
    print("nested comprehension: {}".format(nested_comp_time))
    print("-" * 50)
