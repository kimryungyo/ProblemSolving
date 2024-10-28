from itertools import combinations
from math import lcm

numbers = list(map(int, input().split()))

result = float('inf')
for comb in combinations(numbers, 3):
    temp = lcm(comb[0], comb[1])
    temp = lcm(temp, comb[2])
    result = min(result, temp)

print(result)