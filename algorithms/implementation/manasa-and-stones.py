test_cases = int(raw_input().strip())
for t in xrange(test_cases):
    n = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())

    possible_values = set()
    for i in xrange(n):
        possible_values.add((n-i-1) * a + i * b)

    print ' '.join(map(str, sorted(list(possible_values))))
