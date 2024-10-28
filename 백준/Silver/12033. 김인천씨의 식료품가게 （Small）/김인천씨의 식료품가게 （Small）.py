from itertools import permutations
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    for pair in permutations(nums, N * 2):
        pair = list(pair)
        prices = []
        while pair:
            price_1, price_2 = sorted([pair.pop(), pair.pop()])
            if price_1 * (4 / 3) == price_2:
                prices.append(price_1)
            else: break
        
        if len(prices) == N:
            print(f"Case #{t}: {' '.join(map(str, sorted(prices)))}")
            break