#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))


c_sorted = sorted(c)
distances = [c_sorted[0], n-c_sorted[-1]-1]
for i in xrange(m-1):
    distances.append((c_sorted[i+1] - c_sorted[i])/2)

print max(distances)
