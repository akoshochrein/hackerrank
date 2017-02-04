#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

def get_common_prefix_len(s1, s2):
    idx = 0
    min_len = min(len(s1), len(s2))
    while idx < min_len and s1[idx] == s2[idx]:
        idx += 1
    return idx

common_prefix_len = get_common_prefix_len(s, t)
s_len, t_len = len(s), len(t)
s_length_without_prefix, t_length_without_prefix = s_len - common_prefix_len, t_len - common_prefix_len

result = 'No'
if s_length_without_prefix + t_length_without_prefix > k:
    result = 'No'
elif (s_length_without_prefix + t_length_without_prefix) % 2 == k % 2:
    result = 'Yes'
elif k - common_prefix_len >= 0 and s_length_without_prefix == 0 and t_length_without_prefix == 0:
    result = 'Yes'
elif common_prefix_len >= 0 and k > s_len + t_len:
    result = 'Yes'

print result
