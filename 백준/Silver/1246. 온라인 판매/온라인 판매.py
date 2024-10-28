from sys import stdin
input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())

prices = [ int(input()) for _ in range(m) ]
prices.sort()

customers = m
max_income = 0
sell_price = None

for price in prices:
    income = price * min(customers, n)
    if income > max_income:
        max_income = income
        sell_price = price
    customers -= 1

print(sell_price, max_income)