from functools import cmp_to_key


def compare_string_numbers(a, b):
    if len(a) > len(b):
        return 1
    elif len(b) > len(a):
        return -1
    else:
        # here we need to check from the start of the string and determine which number is bigger
        for i in range(len(a)):
            num_a = int(a[i])
            num_b = int(b[i])
            if num_a > num_b:
                return 1
            elif num_b > num_a:
                return -1
        return 1


def big_sorting(unsorted):
    return sorted(unsorted, key=cmp_to_key(compare_string_numbers))


print(
    big_sorting(
        [
            "1",
            "2",
            "100",
            "12303479849857341718340192371",
            "3084193741082937",
            "3084193741082938",
            "111",
            "200",
        ]
    )
)
