#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n),int(k)]
    arrival_times = map(int,raw_input().strip().split(' '))

    students_on_time = len(filter(lambda t: t < 1, arrival_times))
    print 'NO' if students_on_time > k-1 else 'YES'
