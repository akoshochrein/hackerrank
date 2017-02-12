#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)

    found = False
    for i in xrange(R-r+1):
        found_index = -1
        for k in xrange(C-c+1):
            if G[i][k:k+c] == P[0]:
                found_index = k

            if found_index > -1:
                if all(G[i+l][found_index:found_index+c] == P[l] for l in xrange(r)):
                    found = True
                else:
                    found_index = -1

    print 'YES' if found else 'NO'
