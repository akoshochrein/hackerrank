from collections import Counter


def count_disjunct_letters_to_remove(letter_frequency_first, letter_frequency_second):
    first_letters = set(letter_frequency_first.keys())
    second_letters = set(letter_frequency_second.keys())
    disjunct_letters = first_letters.symmetric_difference(second_letters)

    remove_counter = 0
    for letter in disjunct_letters:
        if letter in first_letters:
            remove_counter += letter_frequency_first[letter]
        else:
            remove_counter += letter_frequency_second[letter]

    return remove_counter


def count_common_letters_to_remove(letter_frequency_first, letter_frequency_second):
    first_letters = set(letter_frequency_first.keys())
    second_letters = set(letter_frequency_second.keys())
    common_letters = first_letters.intersection(second_letters)

    remove_counter = 0
    for letter in common_letters:
        remove_counter += abs(
            letter_frequency_first[letter] - letter_frequency_second[letter]
        )

    return remove_counter


def making_anagrams(s1, s2):
    letter_frequency_first = Counter(s1)
    letter_frequency_second = Counter(s2)

    return count_disjunct_letters_to_remove(letter_frequency_first, letter_frequency_second) + \
        count_common_letters_to_remove(letter_frequency_first, letter_frequency_second)


print(making_anagrams(
    'absdjkvuahdakejfnfauhdsaavasdlkj',
    'djfladfhiawasdkjvalskufhafablsdkashlahdfa')
)
