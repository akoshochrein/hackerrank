# 91011 -> 9 10 11
# 91011 -> 91 01 1

# 99100 -> 99 100

# 101103 -> 1 0 1 1 0 3
# 101103 -> 10 11 03
# 101103 -> 101 103


def is_beautiful(next_number, s):
    if s.startswith(next_number):
        return is_beautiful(str(int(next_number) + 1), s[len(next_number) :])
    return len(s) == 0


def separate_the_numbers(s):
    number_of_digits = 1
    while number_of_digits < len(s) // 2 + 1:
        start_number = s[:number_of_digits]
        if is_beautiful(start_number, s):
            return "YES " + start_number
        number_of_digits += 1
    return "NO"


print(separate_the_numbers("99910001001"))
