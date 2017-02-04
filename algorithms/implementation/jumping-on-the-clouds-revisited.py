#!/bin/python

import sys


n, k = raw_input().strip().split(' ')
n, k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

total_energy = 100
location = 0
while True:
    total_energy -= 1
    location = (location + k) % n
    if c[location] == 1:
        total_energy -= 2
    if location == 0:
        break

print total_energy
