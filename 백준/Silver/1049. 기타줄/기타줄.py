from sys import stdin
input = lambda: stdin.readline().rstrip()

from math import ceil
n, m = map(int, input().split())

pack_prices = []
each_prices = []

for _ in range(m):
    pack, each = map(int, input().split())
    pack_prices.append(pack)
    pack_prices.append(each * 6)
    each_prices.append(each)

best_pack = min(pack_prices)
best_each = min(each_prices)

payment_pack = (n // 6) * best_pack
payment_each = (n % 6) * best_each

all_pack = ceil(n / 6) * best_pack
best = min(all_pack, payment_pack + payment_each)
print(best)