
number_of_tests = int(raw_input().strip())
for _ in xrange(number_of_tests):
    n, m, s = map(int, raw_input().strip().split(' '))
    print (s - 1 + m - 1) % n + 1
