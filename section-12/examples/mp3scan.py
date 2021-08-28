#!/usr/bin/env python

import os
import fnmatch
import musiclib

# define a generator for finding files
def find_files(start_dir, extension):
    for path, directories, files in os.walk(start_dir, topdown=True):
        for file in fnmatch.filter(files, "*{}".format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


# declare generator for finding files containing music data
start_path = input("Specify the directory to scan: ")
my_music_files = find_files(start_path, ".emp3")

for f in my_music_files:
    try:
        reader = musiclib.Reader(f)
        print("performer: {}, album: {}, track: {}, title: {}".format(
            reader.get_value("performer"),
            reader.get_value("album"),
            reader.get_value("track"),
            reader.get_value("title")))
    except Exception as e:
        print(e)
