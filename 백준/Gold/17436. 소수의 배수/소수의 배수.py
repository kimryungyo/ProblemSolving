from math import lcm
from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

counts = 0
for num in nums: counts += m // num

combs = []
for r in range(2, len(nums) + 1):
    combs.extend(combinations(nums, r))

for comb in combs:
    counts += (m // lcm(*comb)) * ( (-1) ** (len(comb) - 1) )

print(counts)