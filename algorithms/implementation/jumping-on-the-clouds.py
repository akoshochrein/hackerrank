#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

jumps, location = 0, 0
while location != n - 1:
    jumps += 1
    if location + 2 < n and c[location+2] == 0:
        location += 2
    else:
        location += 1

print jumps
