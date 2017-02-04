#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

in_between_numbers = []
max_in_b = max(b)
for x in xrange(1, max_in_b + 1):
    all_a_are_factors_in_x = all(x % i_a == 0 for i_a in a)
    x_is_factor_for_all_in_b = all(i_b % x == 0 for i_b in b)
    if all_a_are_factors_in_x and x_is_factor_for_all_in_b:
        in_between_numbers.append(x)

print len(in_between_numbers)
