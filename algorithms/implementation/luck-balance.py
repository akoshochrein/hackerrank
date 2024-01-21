def luck_balance(k, contests):
    unimportant = [contest for contest in contests if contest[1] == 0]
    important = [contest for contest in contests if contest[1] == 1]

    important = sorted(important, key=lambda x: x[0], reverse=True)

    luck = 0
    for contest in unimportant:
        luck += contest[0]

    for contest in important[:k]:
        luck += contest[0]

    for contest in important[k:]:
        luck -= contest[0]

    return luck


contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luck_balance(3, contests))
