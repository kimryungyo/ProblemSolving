n = int(input())
profits = list(map(int, input().split()))
prices = list(map(int, input().split()))

max_profit = max(profits)

second_profits = profits.copy()
second_profits.pop(second_profits.index(max_profit))

second_profit = max(second_profits)

results = []

for i in range(n):
    if profits[i] == max_profit: opportunity_cost = second_profit - prices[i]
    else: opportunity_cost = max_profit - prices[i]

    net_profit = profits[i] - opportunity_cost - prices[i]
    results.append(str(net_profit))

print(" ".join(results))