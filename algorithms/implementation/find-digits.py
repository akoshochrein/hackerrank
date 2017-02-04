#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    total_divisors = 0
    for digit in map(int, str(n)):
        if digit != 0 and n % digit == 0:
            total_divisors += 1
    print total_divisors
