n, target, *coins = map(int, open(0).read().split())
coins.reverse()
count = 0

for coin in coins:
    use = target // coin
    count += use
    target -= use * coin

print(count)