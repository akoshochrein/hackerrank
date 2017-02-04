#!/bin/python

import sys
from collections import deque

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
a_rotated = deque(a)
a_rotated.rotate(k)

for a0 in xrange(q):
    m = int(raw_input().strip())
    print a_rotated[m]
