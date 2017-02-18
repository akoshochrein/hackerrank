
t = int(raw_input().strip())

def is_funny(s):
    rs = s[::-1]
    return all(abs(ord(s[i]) - ord(s[i-1])) == abs(ord(rs[i]) - ord(rs[i-1])) for i in xrange(1, len(s)))

for _ in xrange(t):
    s = raw_input().strip()
    print 'Funny' if is_funny(s) else 'Not Funny'
