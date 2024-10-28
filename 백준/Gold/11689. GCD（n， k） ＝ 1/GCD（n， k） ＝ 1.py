from math import lcm
from itertools import combinations

def prime(n):
    prime_factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1

        else:
            n //= i
            prime_factors.add(i)

    if n > 1: prime_factors.add(n)
    
    return sorted(prime_factors)


n = int(input())
nums = prime(n)

def get_counts(target):
    counts = 0
    for num in nums: counts += target // num

    combs = []
    for r in range(2, len(nums) + 1):
        combs.extend(combinations(nums, r))

    for comb in combs:
        counts += (target // lcm(*comb)) * ( (-1) ** (len(comb) - 1) )
    
    return counts

print( n - get_counts(n) )