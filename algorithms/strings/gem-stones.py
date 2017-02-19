import string

n = int(raw_input().strip())
gem_element_tracker = {c: 0 for c in string.lowercase}

for _ in xrange(n):
    gem_word = raw_input().strip()
    for c in set(gem_word):
        gem_element_tracker[c] += 1

print len(filter(lambda v: v == n, gem_element_tracker.values()))
