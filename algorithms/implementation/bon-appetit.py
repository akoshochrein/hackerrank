# Enter your code here. Read input from STDIN. Print output to STDOUT

n, k = raw_input().strip().split(' ')
n, k = int(n), int(k)
items_cost = map(int,raw_input().strip().split(' '))
charged = int(raw_input().strip())

total = sum(items_cost)
total_without_annas = total - items_cost[k]
split_cost = total_without_annas / 2
answer = 'Bon Appetit'
if charged > split_cost:
    answer = charged - split_cost

print answer
