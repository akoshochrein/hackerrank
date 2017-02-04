#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))


def get_fruit_on_house(fruits, tree_location):
    fruit_that_fell_on_the_house = 0
    for fruit in fruits:
        d = tree_location + fruit
        if d >= s and d <= t:
            fruit_that_fell_on_the_house += 1
    return fruit_that_fell_on_the_house


print get_fruit_on_house(apples, a)
print get_fruit_on_house(oranges, b)
