from itertools import combinations
from math import comb
def homo(n, r): return comb(n + r - 1, r)

N, S = map(int, input().split())
flowers = list(map(int, input().split()))

total = homo(N, S)

others = 0
for over in range(1, N + 1):
    other = 0
    for houses in combinations(range(N), over):
        needs = S
        for house in houses:
            needs -= flowers[house] + 1
        if needs >= 0: other += homo(N, needs)

    if over % 2 == 1: others += other
    else: others -= other

print((total - others) % (10 ** 9 +7))