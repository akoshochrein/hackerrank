#!/bin/python

import re
import string
import sys

s = raw_input().strip()

print len(re.findall('|'.join(list(string.uppercase)), s)) + 1
