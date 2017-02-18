#!/bin/python

import sys
import string

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

encrypted = ''
for c in s:
    letters = string.uppercase if c.isupper() else string.lowercase
    encrypted += letters[(letters.find(c) + k) % 26] if c in string.letters else c

print encrypted
