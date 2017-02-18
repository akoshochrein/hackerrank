#!/bin/python

import sys
from itertools import combinations


s_len = int(raw_input().strip())
s = raw_input().strip()

max_length = 0
unique_chars = list(set(s))
for pair in combinations(unique_chars, 2):
    attempt = ''.join(c for c in s if c in pair)
    if all(attempt[i-1] != attempt[i] for i in xrange(1, len(attempt))):
        if len(attempt) > max_length:
            max_length = len(attempt)

print max_length
