#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

total_evenly_divisible_pairs = 0
for i in xrange(n):
    for j in xrange(i + 1, n):
        if (a[i] + a[j]) % k == 0:
            total_evenly_divisible_pairs += 1

print total_evenly_divisible_pairs
