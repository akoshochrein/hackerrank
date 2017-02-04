#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positives, negatives, zeros = 0, 0, 0
for i in arr:
    if i > 0:
        positives += 1
    elif i < 0:
        negatives += 1
    else:
        zeros += 1

print positives/float(n)
print negatives/float(n)
print zeros/float(n)
