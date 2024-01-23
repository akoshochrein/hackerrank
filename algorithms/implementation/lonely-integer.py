from collections import Counter


def lonely_integer(numbers: list[int]) -> int:
    numbers_frequency = Counter(numbers)
    for number, frequency in numbers_frequency.items():
        if frequency == 1:
            return number


print(lonely_integer([1, 2, 3, 4, 3, 2, 1]))
