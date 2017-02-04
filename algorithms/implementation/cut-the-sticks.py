#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while len(arr):
    min_cut = min(arr)
    print len(arr)
    arr = filter(lambda s: s > 0, map(lambda s: s - min_cut, arr))
