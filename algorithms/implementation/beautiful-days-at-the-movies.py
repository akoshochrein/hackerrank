# Enter your code here. Read input from STDIN. Print output to STDOUT

i, j, k = map(int, raw_input().strip().split(' '))

total_beautiful_days = 0
for day in xrange(i, j + 1):
    day_reversed = int(str(day)[::-1])
    if abs(day - day_reversed) % k == 0:
        total_beautiful_days += 1

print total_beautiful_days
