from collections import Counter
from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())
nums = dict(Counter(map(int, input().split())))
x = int(input())

count = 0
for num in nums.keys():
    other = x - num
    if other in nums:
        count += nums[other]
        if num == other:
            count -= 1

print(count // 2)