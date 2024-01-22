def find_the_median(unsorted_list):
    sorted_array = sorted(unsorted_list)
    middle_index = len(sorted_array) // 2

    return sorted_array[middle_index]


print(find_the_median([5, 3, 1, 2, 4]))
