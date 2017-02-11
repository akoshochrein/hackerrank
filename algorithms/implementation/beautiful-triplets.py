n, d = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))

s = set(a)
beautiful_triplet_count = 0
for i in s:
    if d + i in s and i - d in s:
        beautiful_triplet_count += 1


print beautiful_triplet_count
