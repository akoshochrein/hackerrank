from math import sqrt, floor, ceil

num_test_cases = int(raw_input().strip())
for _ in xrange(num_test_cases):
    a, b = map(int, raw_input().strip().split(' '))
    print int(floor(sqrt(b)) - ceil(sqrt(a)) + 1)
