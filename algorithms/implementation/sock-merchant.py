#!/bin/python

import sys
from collections import defaultdict


n = int(raw_input().strip())
colors = map(int,raw_input().strip().split(' '))

total_sold = 0
sock_count_by_color = defaultdict(int)
for color in colors:
    if sock_count_by_color[color] == 1:
        sock_count_by_color[color] = 0
        total_sold += 1
    else:
        sock_count_by_color[color] = 1

print total_sold
