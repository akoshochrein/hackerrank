#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n, c, m = raw_input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]

    surplus_wrappers = n // c
    total_chocolates_exchanged = surplus_wrappers
    while True:
        current_exchanged = surplus_wrappers // m
        total_chocolates_exchanged += current_exchanged
        if current_exchanged == 0:
            break
        surplus_wrappers = current_exchanged + surplus_wrappers % m
    print total_chocolates_exchanged
