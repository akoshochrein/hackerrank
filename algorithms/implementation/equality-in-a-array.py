from collections import Counter


n = int(raw_input().strip())
elements = map(int, raw_input().strip().split(' '))

frequencies = Counter(elements)
print n - max(frequencies.values())
