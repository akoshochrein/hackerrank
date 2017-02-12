#!/bin/python

import sys
from collections import Counter

Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()

    board_frequency = Counter(b)
    everyone_has_a_friend = all(v > 1 and k != '_' for k, v in board_frequency.iteritems())
    everyone_has_a_neighbour = all(b[i] == b[i-1] or b[i] == b[i+1] for i in xrange(1, n-1))
    is_happy_state = everyone_has_a_friend and everyone_has_a_neighbour
    if len(board_frequency) == 1 and board_frequency.keys()[0] != '_':
        print 'NO'
    elif is_happy_state:
        print 'YES'
    elif '_' not in board_frequency:
        print 'NO'
    elif any(v == 1 and k != '_' for k, v in board_frequency.iteritems()):
        print 'NO'
    else:
        print 'YES'
