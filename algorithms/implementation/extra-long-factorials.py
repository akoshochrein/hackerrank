#!/bin/python

import sys


n = int(raw_input().strip())

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print factorial(n)
