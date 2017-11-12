#!/usr/bin/env python

num = "9,223,372,036,854,775,807"

for i in range(0, len(num)):
    if num[i] in '0123456789':
        print(num[i], end = '')
