from math import lcm
from itertools import combinations

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

counts = 0
for num in nums: counts += n // num

combs = []
for r in range(2, len(nums) + 1):
    combs.extend(combinations(nums, r))

for comb in combs:
    counts += (n // lcm(*comb)) * ( (-1) ** (len(comb) - 1) )

print(n - counts)