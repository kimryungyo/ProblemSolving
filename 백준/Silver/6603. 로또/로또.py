from itertools import combinations

while True:
    n, *nums = list(map(int, input().split()))
    if n == 0: break

    combs = list(combinations(nums, 6))
    for comb in combs: print(' '.join(map(str, comb)))
    print()