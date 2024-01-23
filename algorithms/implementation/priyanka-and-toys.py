CONTAINER_BUFFER = 4


def priyanka_and_toys(weights: list[int]) -> int:
    if len(weights) == 0:
        return 0

    number_of_containers = 1
    sorted_weights = sorted(weights)
    current_container_maximum_weight = sorted_weights[0] + CONTAINER_BUFFER
    for i in range(len(sorted_weights)):
        weight = sorted_weights[i]
        if weight > current_container_maximum_weight:
            number_of_containers += 1
            current_container_maximum_weight = weight + CONTAINER_BUFFER

    return number_of_containers


print(priyanka_and_toys([1, 2, 3, 21, 7, 12, 14, 21]))
