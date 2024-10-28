from math import lcm
from itertools import combinations

n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

removes = set()
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] % nums[i] == 0:
            removes.add(nums[j])

for num in removes: nums.remove(num)



counts = 0
for num in nums: counts += n // num

combs = []
for r in range(2, len(nums) + 1):
    combs.extend(combinations(nums, r))

for comb in combs:
    counts += (n // lcm(*comb)) * ( (-1) ** (len(comb) - 1) )

print(counts)