#!/usr/bin/env python

import os

start_dir = "."

for path, directories, files in os.walk(start_dir, topdown = True):
    print(path)

    for f in files:
        print("\t{}".format(f))
