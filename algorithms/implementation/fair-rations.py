#!/bin/python

import sys


N = int(raw_input().strip())
B = map(int,raw_input().strip().split(' '))

if sum(B) % 2 == 1:
    print 'NO'
else:
    steps = 0
    for index, item in enumerate(B):
        if item % 2 == 1:
            B[index + 1] += 1
            B[index] += 1
            steps += 1
    print steps * 2
