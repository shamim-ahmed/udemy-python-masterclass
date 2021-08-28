#!/usr/bin/env python

import os
import fnmatch

# define generator for file search
def find_files(start_dir, extension):
    for path, directories, files in os.walk(start_dir, topdown=True):
        for file in fnmatch.filter(files, "*{}".format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


# declare generator for file search
fgen = find_files(".", ".py")

try:
    while True:
        print(next(fgen))
except StopIteration:
    pass
