def two_strings(first, second):
    letters_first = set(first)
    letters_second = set(second)

    common_letters = letters_first.intersection(letters_second)

    return "YES" if len(common_letters) != 0 else "NO"


print(two_strings("hello", "world"))
