def icecream_parlor(m, prices):
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] == m:
                return [i + 1, j + 1]


print(icecream_parlor(6, [1, 4, 5, 3, 2]))
