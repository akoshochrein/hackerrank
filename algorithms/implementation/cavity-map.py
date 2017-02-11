#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)

new_grid = []
for i in xrange(n):
    new_grid.append([])
    for j in xrange(n):
        new_grid[i].append(grid[i][j])

for i in xrange(1, n-1):
    for j in xrange(1, n-1):
        pivot = grid[i][j]
        if all(grid[k][l] < pivot for k, l in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]):
            new_grid[i][j] = 'X'

for i in xrange(n):
    print ''.join(map(str, new_grid[i]))
