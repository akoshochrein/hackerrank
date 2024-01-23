def closest_numbers(numbers: list[int]) -> list[int]:
    sorted_numbers = sorted(numbers)

    min_difference = None
    pairs_with_min_difference = []
    for i in range(len(sorted_numbers) - 1):
        first, second = sorted_numbers[i], sorted_numbers[i + 1]
        difference = second - first
        if min_difference is None or difference < min_difference:
            min_difference = difference
            pairs_with_min_difference = [first, second]
        elif difference == min_difference:
            pairs_with_min_difference.extend([first, second])

    return sorted(pairs_with_min_difference)


print(closest_numbers([5, 4, 3, 2, 1]))
