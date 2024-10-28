from itertools import combinations
from math import lcm

n = int(input())
count = 0

divisors = [ 11 ]
for i in range(len(str(n)) - 2):
    div = divisors[-1] * 10 + 1
    divisors.append(div)

for length in range(1, len(divisors) + 1):
    combs = combinations(divisors, length)
    for comb in combs:
        count -= (n // lcm(*comb)) * ( (-1) ** length )

print(count)