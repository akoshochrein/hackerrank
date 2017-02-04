#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

values = [a, b, c, d, e]
total = sum(values)
min_value = min(values)
max_value = max(values)

print total - max_value, total - min_value
