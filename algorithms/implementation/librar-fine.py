#!/bin/python

import sys
import datetime

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

def returned_in_time(return_date, due_date):
    same_year = return_date[0] == due_date[0]
    same_month = return_date[1] == due_date[1]
    just_in_time = False

    if return_date[0] < due_date[0]:
        just_in_time = True
    elif same_year and return_date[1] < due_date[1]:
        just_in_time = True
    elif same_year and same_month and return_date[2] <= due_date[2]:
        just_in_time = True

    return just_in_time

fine = 0
if returned_in_time((y1, m1, d1), (y2, m2, d2)):
    fine = 0
elif y1 > y2:
    fine = 10000
elif m1 > m2:
    fine = (m1 - m2) * 500
elif d1 > d2:
    fine = (d1 - d2) * 15

print fine
