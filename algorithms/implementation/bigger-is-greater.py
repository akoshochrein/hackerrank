
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def next_permutation(s):
    i = len(s) - 1
    while i > 0 and s[i-1] >= s[i]:
        i -= 1
    if i < 1:
        return None

    j = len(s) - 1
    while s[j] <= s[i-1]:
        j -= 1
    s[i-1], s[j] = s[j], s[i-1]

    s[i:] = s[i:][::-1]
    return s

test_cases = int(raw_input().strip())
for _ in xrange(test_cases):
    word = raw_input().strip()
    s = next_permutation(list(word))
    if s is not None:
        print ''.join(s)
    else:
        print 'no answer'
