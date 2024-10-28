n, *prices = map(int, open(0).read().split())
prices.sort(reverse=True)
paid = 0

stack = 0
for price in prices:
    stack += 1

    if stack == 3: stack = 0
    else: paid += price

print(paid)