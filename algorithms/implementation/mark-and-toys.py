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


def mark_and_toys_expensive(budget: int, prices: list[int]) -> int:
    sorted_prices = sorted(prices, reverse=True)

    purchased_toy_prices = []
    wallet = budget
    for price in sorted_prices:
        if wallet - price >= 0:
            wallet -= price
            purchased_toy_prices.append(price)

    return len(purchased_toy_prices)


print(mark_and_toys_expensive(50, [1, 12, 5, 40, 111, 200, 1000, 10]))
