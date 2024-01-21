from collections import Counter


def string_construction(start_string):
    letter_frequency = Counter(start_string)
    return len(letter_frequency.keys())


print(string_construction("abab"))
