#!/usr/bin/env python

num = "9,223,372,036,854,775,807"

for i in range(0, len(num)):
    if '0' <= num[i] <= '9':
        print(num[i])
