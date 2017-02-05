#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

print s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')
