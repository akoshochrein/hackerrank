#!/bin/python

import sys
from math import sqrt, floor, ceil


s = raw_input().strip()
spaceless = s.replace(' ', '')
sqrt_l = sqrt(len(spaceless))
rows, columns = int(floor(sqrt_l)), int(ceil(sqrt_l))
limit = max(rows, columns)

encrypted_words = []
for i in xrange(limit):
    encrypted_words.append(spaceless[i::limit])

print ' '.join(encrypted_words)
