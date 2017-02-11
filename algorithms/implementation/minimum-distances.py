#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

min_distance_found = False
min_distance = -1
for i, i_num in enumerate(A):
    for j, j_num in enumerate(A):
        if i_num == j_num and i != j:
            distance = abs(i - j)
            if distance < min_distance or not min_distance_found:
                min_distance = distance
                min_distance_found = True
print min_distance
