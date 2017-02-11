#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

EXACT_HOUR = '{hour} o\' clock'
EXACT_QUARTER_PAST = 'quarter past {hour}'
BEFORE_HALF = '{minutes} minutes past {hour}'
EXACT_HALF_HOUR = 'half past {hour}'
PAST_HALF = '{minutes} minutes to {hour}'
EXACT_QUARTER_TO = 'quarter to {hour}'

def get_number_to_string(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif n == 21:
        return 'twenty one'
    elif n == 22:
        return 'twenty two'
    elif n == 23:
        return 'twenty three'
    elif n == 24:
        return 'twenty four'
    elif n == 25:
        return 'twenty five'
    elif n == 26:
        return 'twenty six'
    elif n == 27:
        return 'twenty seven'
    elif n == 28:
        return 'twenty eight'
    elif n == 29:
        return 'twenty nine'

if m == 0:
    print EXACT_HOUR.format(hour=get_number_to_string(h))
elif m == 15:
    print EXACT_QUARTER_PAST.format(hour=get_number_to_string(h))
elif m < 30:
    print BEFORE_HALF.format(minutes=get_number_to_string(m), hour=get_number_to_string(h))
elif m == 30:
    print EXACT_HALF_HOUR.format(hour=get_number_to_string(h))
elif m == 45:
    print EXACT_QUARTER_TO.format(hour=get_number_to_string(h+1))
elif m > 30:
    print PAST_HALF.format(minutes=get_number_to_string(60-m), hour=get_number_to_string(h+1))
