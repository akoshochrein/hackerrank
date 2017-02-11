from math import ceil, floor

p = int(raw_input().strip())
q = int(raw_input().strip())

def check_if_kaprekar(n, rounding):
    number = n ** 2
    split_here = int(rounding(len(str(number))/2.0))
    first_part = int(str(number)[:split_here] or 0)
    second_part = int(str(number)[split_here:] or 0)
    if first_part + second_part == i:
        if len(str(number)) == 1 or (second_part != 0 and len(str(number)) != 1):
            return True
    return False


kaprekar_numbers_in_range = []
for i in xrange(p, q + 1):
    if check_if_kaprekar(i, floor) or check_if_kaprekar(i, ceil):
        kaprekar_numbers_in_range.append(i)


if len(kaprekar_numbers_in_range) > 0:
    print ' '.join(map(str, kaprekar_numbers_in_range))
else:
    print 'INVALID RANGE'
