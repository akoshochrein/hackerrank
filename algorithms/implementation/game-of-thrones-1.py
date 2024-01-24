from collections import Counter


def game_of_thrones_one(key: str) -> str:
    letter_frequencies = Counter(key)

    odd_letters = 0
    for letter in letter_frequencies.keys():
        if letter_frequencies[letter] % 2 != 0:
            odd_letters += 1

    if odd_letters > 1:
        return "NO"

    return "YES"


print(game_of_thrones_one("cdcdcdcdeeeef"))


# anagram: cat -> tac -> atc -> act -> tca -> cta
# palindrome: tacocat, anna
