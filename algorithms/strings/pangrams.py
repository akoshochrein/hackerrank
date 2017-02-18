from string import letters

s = raw_input().strip()
letter_counter = {l: 0 for l in letters[:26]}
for c in s.lower():
    if c in letter_counter:
        letter_counter[c] += 1

print 'pangram' if all(v > 0 for v in letter_counter.values()) else 'not pangram'
