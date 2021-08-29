#!/usr/bin/env python

text = "what have the romans ever done for us"

capitals = [c.upper() for c in text]
print(capitals)

capital_words = [w.upper() for w in text.split(" ")]
print(capital_words)

lc_words = text.split(" ")
print(lc_words)

lc_words = [word for word in text.split(" ")]
print(lc_words)
