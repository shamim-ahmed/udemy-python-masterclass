#!/usr/bin/env python

ip_addr = input("Please enter the IP address: ")
current_segment = ''
segment_count = 0

for c in ip_addr:
    if c == '.':
        segment_count += 1
        print("segment {0} contains {1} characters".format(segment_count, len(current_segment)))
        current_segment = ''
    else:
        current_segment += c
        
#this is for the last component
if current_segment != '':
    segment_count += 1
    print("segment {0} contains {1} characters".format(segment_count, len(current_segment)))
