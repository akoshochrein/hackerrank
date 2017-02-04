#!/bin/python

import sys
import string


h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
letter_to_height = {l: h[i] for i, l in enumerate(string.letters[:26])}

tallest_letter_height = 0
for letter in word:
    if letter_to_height[letter] > tallest_letter_height:
        tallest_letter_height = letter_to_height[letter]

print len(word) * tallest_letter_height
