def mark_and_toys(budget: int, prices: list[int]) -> int:
    sorted_prices = sorted(prices)

    number_of_toys = 0
    wallet = budget
    for price in sorted_prices:
        if wallet - price >= 0:
            wallet -= price
            number_of_toys += 1
        else:
            break

    return number_of_toys


print(mark_and_toys(50, [1, 12, 5, 111, 200, 1000, 10]))
