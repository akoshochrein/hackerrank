#!/bin/python

import sys


s = raw_input().strip()
errors = 0
for i in xrange(len(s)):
    should_be_s = i % 3 == 0 or i % 3 == 2
    should_be_o = not should_be_s
    if should_be_o and s[i] != 'O' or should_be_s and s[i] != 'S':
        errors += 1

print errors
