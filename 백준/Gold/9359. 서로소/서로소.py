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

tc = int(input())

for tcn in range(1, tc + 1):
    a, b, n = map(int, input().split())

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
    
    a_c = get_counts(a-1)
    b_c = get_counts(b)

    print(f"Case #{tcn}:", (b - a + 1) - (b_c - a_c))