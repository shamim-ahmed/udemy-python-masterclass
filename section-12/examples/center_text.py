#!/usr/bin/env python

def center_text(*args):
    result = "-".join([str(arg) for arg in args])
    left_padding = (80 - len(result)) // 2
    print(" " * left_padding, result, sep="")


# invoke with varargs
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text(12)
center_text("spam, spam, spam and spam")
center_text("first", "second", 3, 4, "spam")
