#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic.append(int(raw_input().strip(), 2))

max_topic_teams, max_topic_value = 0, 0
for i in xrange(n):
    for j in xrange(i + 1, n):
        current_topic_value = bin(topic[i] | topic[j]).count('1')
        if current_topic_value > max_topic_value:
            max_topic_teams, max_topic_value = 1, current_topic_value
        elif current_topic_value == max_topic_value:
            max_topic_teams += 1

print max_topic_value
print max_topic_teams
