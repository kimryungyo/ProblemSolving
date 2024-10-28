N = int(input())
prices = list(map(int, input().split()))

max_profit = 0

min_price = prices[0]

for i in range(1, N):
    max_profit = max(max_profit, prices[i] - min_price)
    
    min_price = min(min_price, prices[i])

print(max_profit)