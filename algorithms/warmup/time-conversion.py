#!/bin/python

import sys


time = raw_input().strip()

daytime = time[8:10]
hours, minutes, seconds = time[:8].split(':')
if (daytime == 'PM' and hours != '12') or (daytime == 'AM' and hours == '12'):
    hours = int(hours)
    hours = (hours + 12) % 24
    hours = str(hours).zfill(2)

print ':'.join([hours, minutes, seconds])
