from collections import defaultdict

n, k = map(int, raw_input().strip().split(' '))
s = map(int, raw_input().strip().split(' '))

# I admit, I had to read the forums a lot to understand this one

frequencies = [0] * k
for i in s:
    frequencies[i % k] += 1

ans = min(frequencies[0], 1)
for i in xrange(1, k//2 + 1):
    if i != k - i:
        ans += max(frequencies[i], frequencies[k-i])
    elif frequencies[i]:
        ans += 1

print ans
